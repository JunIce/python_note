#!/usr/bin/python
#coding=utf8

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient(host='0.0.0.0',port=27017)
db=client.jdfc

def listPage(page):
    url='http://www.jddyfw.com/sale.php?page=%s'%page
    r=requests.get(url)
    r.encoding='gb2312'

    soup=BeautifulSoup(r.text, "html.parser")
    mainTable=soup.find('table',cellpadding="2")
    itemList=mainTable.find_all('tr', height="27")
    links=[]
    for item in itemList:
        alink=item.find('a')
        infoHref=alink.get('href')
        links.append({"href": infoHref})
    print(links)
    db.urlcollections.insert_many(links)

for i in range(1,200):
    listPage(i)