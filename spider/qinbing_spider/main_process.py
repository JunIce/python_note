#coding=utf-8
from multiprocessing import Pool
from list_page import getUrls,get_page_content,get_page_content_ori
from RdPool import RdsPool

class MainProcess():
  def __init__(self, q, max_process=6):
    self.__q = q
    self.__p = Pool(max_process)
    self.__redis = RdsPool()
    self.urls = []
    self.__initurl = 'https://www.qinbing.cn/Portal/Index/news/page/{}/type/357'
    self.list_url_init()

  '''爬虫列表页链接初始化'''
  def list_url_init(self):
    for i in range(0,476):
      url = self.__initurl.format(i)
      self.urls.append(url)

  def go(self):
    for url in self.urls:
      self.__p.apply_async(getUrls, args=(url,))
    self.__p.close()
    self.__p.join()

  def doContents(self):
    for i in range(3415, 3792):
      url = 'https://www.qinbing.cn' + self.__redis.lindex('page_url_new', i).decode('utf-8')
      self.__p.apply_async(get_page_content, args=(url,))
    self.__p.close()
    self.__p.join()


