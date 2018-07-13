#!/usr/bin/python
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import pymysql
import threading
import time
'''
豆瓣top 250抓取
url基本格式 https://book.douban.com/top250?start=25
其中start值以params方式传入
demo3实现多线程抓取
'''
pattern = re.compile('\d+')


def getHTMLDom(page=0):
  urlBase = 'https://book.douban.com/top250'
  headers = {
      'User-Agent':
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
  }
  start = 25 * int(page)
  html = requests.get(urlBase, params={'start': start}, headers=headers).text
  dom = BeautifulSoup(html, 'html.parser')
  # 获取目标node
  return dom


def parseToDict(node):
  '''
    根据node解析html，并赋值成字典
    通过and or 语法进行删选兼容，预防字段为空时报错
  '''
  n = {}
  n['titlepic'] = node.select('img') and node.select('img')[0].attrs.get(
      'src') or ''
  n['title'] = node.select('a')[1].attrs.get('title') and node.select(
      'a')[1].attrs.get('title') or ''
  n['titleurl'] = node.select('a') and node.select('a')[1].attrs.get(
      'href') or ''
  n['pl_nums'] = node.find(
      'span', attrs={'class': 'pl'}) and re.search(
          pattern,
          node.find('span', attrs={
              'class': 'pl'
          }).string).group() or 0
  n['vote_nums'] = node.select('.rating_nums') and node.select(
      '.rating_nums')[0].string or 0
  n['describe'] = node.select('.inq') and node.select('.inq')[0].string or ''
  s = node.select('.pl')[0].string.split(' / ')  # 此处分隔符左右都加上空格，防止匹配到多价格元素
  if len(s) == 4:  # 如果list不足4为，补齐
    s.insert(1, None)
  pattern1 = re.compile('\d+(\.\d+)?')
  s[4] = re.search(pattern1, s[-1]).group()
  n['writer'], n['translater'], n['publisher'], n['pub_at'], n['price'] = s
  return n


class Db():
  def __init__(self, dbConf):
    self._conn = pymysql.connect(**dbConf)
    self._cursor = self._conn.cursor()

  def query(self, sql, **kw):
    try:
      with self._conn.cursor() as cursor:
        cursor.execute(sql)
      self._conn.commit()
    except Exception:
      raise Exception

  def close(self):
    self._cursor.close()
    self._conn.close()


if __name__ == '__main__':
  dbConf = {
      'host': '127.0.0.1',
      'user': 'root',
      'port': 3310,
      'password': '1',
      'db': 'spider',
      'charset': 'utf8mb4'
  }
  db = Db(dbConf)
  try:
    '''
      删除表
    '''
    dropSql = "DROP TABLE IF EXISTS db_book"
    db.query(dropSql)
  finally:
    # 新建表
    creatSql = '''
      CREATE TABLE `db_book` (
      `id` int(4) NOT NULL AUTO_INCREMENT,
      `title` varchar(100) NOT NULL DEFAULT '',
      `titlepic` varchar(255) NOT NULL DEFAULT '',
      `writer` varchar(255) NOT NULL COMMENT '作者',
      `translater` VARCHAR(20) not null default '',
      `publisher` VARCHAR(20) not null default '',
      `pub_at` VARCHAR(20) not null default '',
      `price` DECIMAL(6,2) NOT null default '0.00',
      `pl_nums` MEDIUMINT(10) NOT NULL default 0,
      `vote_nums` MEDIUMINT(10) not null default 0,
      `titleurl` varchar(50) NOT NULL DEFAULT '',
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
    '''

    db.query(creatSql)

  sql = "INSERT INTO db_book (`title`, `titlepic`, `writer`, `translater`, `publisher`, `pub_at`, `price`, `pl_nums`, `vote_nums`, `titleurl`) VALUES('{title}', '{titlepic}', '{writer}', '{translater}', '{publisher}', '{pub_at}', '{price}', {pl_nums}, {vote_nums}, '{titleurl}')"
  '''
    增加多线程抓取
  '''
  threads = []
  lock = threading.Lock()

  def thread_main(i):
    start = time.time()
    lock.acquire()
    print('线程%d开始时间：%d' % (i, start))
    nodes = getHTMLDom(i).select('.indent table')
    for node in nodes:
      n = parseToDict(node)
      sql1 = sql.format(**n)
      db.query(sql1)
    end = time.time()
    lock.release()
    print('线程%d结束时间：%d' % (i, end))

  for i in range(0, 10):
    t = threading.Thread(target=thread_main, args=(i, ))
    threads.append(t)
    print('线程%d插入完成' % i)

  for j in range(0, 10):
    threads[j].start()

  for z in range(0, 10):
    threads[z].join()

  db.close()
'''
线程0开始时间：1531448544
线程0结束时间：1531448545线程1开始时间：1531448544
线程1结束时间：1531448547线程2开始时间：1531448544
线程2结束时间：1531448549线程3开始时间：1531448544
线程3结束时间：1531448550线程4开始时间：1531448544
线程4结束时间：1531448552线程5开始时间：1531448544
线程5结束时间：1531448553线程6开始时间：1531448544
线程6结束时间：1531448555线程7开始时间：1531448544
线程7结束时间：1531448556线程8开始时间：1531448544
线程8结束时间：1531448558线程9开始时间：1531448544
线程9结束时间：1531448559
'''