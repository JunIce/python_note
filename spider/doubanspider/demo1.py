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
'''
pattern = re.compile('\d+')

def getHTMLDom():
  urlBase = 'https://book.douban.com/top250'
  headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
  html = requests.get(urlBase, data={'start':'50'}, headers=headers).text
  dom = BeautifulSoup(html, 'html.parser')
  # 获取目标node
  return dom

def parseToDict(node):
  '''
    根据node解析html，并赋值成字典
  '''
  n = {}
  n['titlepic'] = node.select('img')[0].attrs.get('src')
  n['title'] = node.select('a')[1].attrs.get('title')
  n['titleurl'] = node.select('a')[1].attrs.get('href')
  n['pl_nums'] = re.search(pattern, node.find('span', attrs={'class':'pl'}).string).group()
  n['vote_nums'] = node.select('.rating_nums')[0].string
  n['describe'] = node.select('.inq')[0].string
  s = node.select('.pl')[0].string.split('/')
  if len(s) == 4: # 如果list不足4为，补齐
    s.insert(1,None)

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
    'user':'root',
    'port': 3310,
    'password': '1',
    'db': 'spider',
    'charset': 'utf8mb4'
  }
  db = Db(dbConf)
  sql = "INSERT INTO db_book (`title`, `titlepic`, `writer`, `translater`, `publisher`, `pub_at`, `price`, `pl_nums`, `vote_nums`, `titleurl`) VALUES('{title}', '{titlepic}', '{writer}', '{translater}', '{publisher}', '{pub_at}', '{price}', {pl_nums}, {vote_nums}, '{titleurl}')"

  nodes = getHTMLDom().select('.indent table')
  for node in nodes:
    n = parseToDict(node)
    sql1 = sql.format(**n)
    db.query(sql1)
    print("插入完成")
  
  db.close()
