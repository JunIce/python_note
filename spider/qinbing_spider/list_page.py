#coding=utf-8
import requests
from bs4 import BeautifulSoup
from RdPool import RdsPool
import re

headers = { 
            'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept - Encoding':'gzip, deflate',
            'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
            'Connection':'Keep-Alive',
            'Host':'zhannei.baidu.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116   Safari/537.36 Edge/15.15063'
          }

redis = RdsPool()

def getUrls(page_url):
  ''' 请求html'''
  html = requests.get(page_url, headers=headers).text
  dom = BeautifulSoup(html, 'html.parser')
  nodes = dom.find_all('div', class_="middle-left")

  urls = []
  for i in nodes:
    url = i.select('a')[1].attrs.get('href')
    redis.lpush('page_url_new', url)
    print(url)

retime = re.compile(r'(\d+)年(\d+)月(\d+)日(\S+)鸡蛋价格行情.*')
recity = re.compile(r'(.*)\<a.*')
def get_page_content(url):
  ''' 请求html'''
  print(url)
  html = requests.get(url, headers=headers).text
  dom = BeautifulSoup(html, 'html.parser')
  time = dom.find('h2').string
  ctime = retime.findall(time)
  print(ctime)
  '''时间初始化'''
  year = ctime[0][0]
  month = ctime[0][1]
  day = ctime[0][2]
  province = ctime[0][3]

  ptime = '{}/{}/{}'.format(year,month,day)

  nodes = dom.find_all('tr')
  print(nodes)
  urls = []
  for node in nodes:
    n = {}
    n['city'] = node.select('td')[0].contents[0] and node.select('td')[0].contents[0] or ''
    n['price'] = node.select('td')[1].string and node.select('td')[1].string.replace('\xa0','') or 0
    n['trend'] = node.select('td')[2].string and node.select('td')[2].string or '-'
    n['year'] = year
    n['month'] = month
    n['day'] = day
    n['time'] = ptime
    n['province'] = province
    redis.lpush('content_new', n)
    print(n)


retime_ori = re.compile(r'(\d+)月(\d+)日(\S+)鸡蛋价格$')
def get_page_content_ori(url):
  ''' 请求html'''
  print(url)
  html = requests.get(url, headers=headers).text
  dom = BeautifulSoup(html, 'html.parser')
  time = dom.find('h2').string
  ctime = retime_ori.findall(time)
  '''时间初始化'''
  year = 2018
  month = ctime[0][0]
  day = ctime[0][1]
  province = ctime[0][2]

  ptime = '{}/{}/{}'.format(year,month,day)

  nodes = dom.find_all('tr')
  urls = []
  for node in nodes:
    n = {}
    n['city'] = node.select('td')[0].contents[0] and node.select('td')[0].contents[0] or ''
    n['price'] = node.select('td')[1].string and node.select('td')[1].string.replace('\xa0','') or 0
    n['trend'] = node.select('td')[2].string and node.select('td')[2].string or '-'
    n['year'] = year
    n['month'] = month
    n['day'] = day
    n['time'] = ptime
    n['province'] = province
    redis.lpush('content_new_ori', n)
    print(n)