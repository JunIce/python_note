#!/usr/bin/python
#coding=utf-8
import requests
from bs4 import BeautifulSoup

base = 'https://www.b7.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0)Gecko/20100101 Firefox/22.0'
}

f = open('url.txt', 'a+')
count = 0
def page_spider(idx):
    global count
    if idx == 1:
        u = '{}/index/index.html'.format(base)
    else:
        u = '{}/index/index_{}.html'.format(base, idx)
    
    r = requests.get(u, headers=headers)
    r.encoding='utf-8'
    html = BeautifulSoup(r.text,"html.parser")
    page_images = html.find_all(class_='img')
    count += len(page_images)
    for img in page_images:
        i = img.find('img')
        f.write(i['src']+'----'+i['alt']+'\n')

if __name__ == '__main__':
    for i in range(1,183):
        page_spider(i)

        