#!/usr/bin/python
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import pymysql
'''
豆瓣top 250抓取
url基本格式 https://book.douban.com/top250?start=25
其中start值以params方式传入
demo2实现多页抓取
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
    增加多页获取，通过循环获取
  '''
  for i in range(0, 9):
    nodes = getHTMLDom(i).select('.indent table')
    for node in nodes:
      n = parseToDict(node)
      sql1 = sql.format(**n)
      db.query(sql1)
      print("插入完成")

  db.close()
