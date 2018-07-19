#!/bin/bash
# -*- coding: utf-8 -*-
# encoding=utf8  
from bs4 import BeautifulSoup
import requests
import importlib
import os
import time
import sys
from urllib.request import urlretrieve

def get_page(buff):
  pages = buff.find(class_='ckqw').find_all('a')
  return len(pages)

def download_image(img_src, img_name):
  urlretrieve(url=img_src, filename = 'images/' + img_name)
  print('下载完成： %s'%img_name)

if __name__ == "__main__":
  headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
  }
  list_url = []
  for num in range(1,2):
    if num == 1:
      url = 'http://www.yuwenziyuan.com/sjb/6s/dzkb/'
    else:
      url = 'http://www.yuwenziyuan.com/sjb/6s/dzkb/list256_%d.html' % num
    req = requests.get(url = url, headers = headers)
    req.encoding = 'gb2312'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    target_url = bf.find_all(class_='mainSoftName')
    for i in target_url:
      list_url.append(i.get_text() + '=' + i.a.get('href'))
  print(list_url)
  print("采集完成")

  cont_url_box = []

  for item in list_url:
    img_info = item.split("=")
    target_url = url + img_info[1]
    img_req = requests.get(url=target_url, headers = headers)
    img_req.encoding = 'gb2312'
    img_text = img_req.text

    img_content_html = BeautifulSoup(img_text, 'lxml')
    total_page = get_page(img_content_html)

    if total_page == 0:
      cont_url = url + img_info[1]
      cont_url_box.append(cont_url)
    else:
      # 获取内容页html名称
      cont_name = img_info[1].split('.')
      for i in range(1,total_page):
        cont_url = url + cont_name[0] + '_%d.html' % i
        cont_url_box.append(cont_url)
  
  print("内容页获取成功")
  print(cont_url_box)

  for i in range(len(cont_url_box)):
    cont_req = requests.get(url=cont_url_box[i], headers = headers)
    cont_req.encoding = 'gb2312'
    cont_text = cont_req.text      
    cont_content_html = BeautifulSoup(cont_text, 'lxml')
    img_src = cont_content_html.find(class_='dzkb').img.get('src')
    download_image(img_src, 'image_' + str(i) + '.jpg')