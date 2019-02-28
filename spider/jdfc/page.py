#!/usr/bin/python
#coding=utf8

import requests

from urllib import parse
from bs4 import BeautifulSoup
from pymongo import MongoClient
from time import sleep
client = MongoClient(host='0.0.0.0',port=27017)
db=client.jdfc

def getPage(u):
    url='http://www.jddyfw.com/%s'%u
    p=requests.get(url)
    p.encoding='gb2312'

    query=parse.urlsplit(url).query
    qs=parse.parse_qs(query)

    soup=BeautifulSoup(p.text, "html.parser")
    mainTable=soup.find_all('table',cellpadding="2")
    if len(mainTable)<= 0:
        return

    # table1
    mainTableTds=mainTable[0].find_all('td')

    newstime=mainTableTds[2].text.strip()
    origin=mainTableTds[6].text.strip()
    position=mainTableTds[10].contents[0].strip()
    name=mainTableTds[12].text.strip()
    ftype=mainTableTds[14].text.strip()
    structure=mainTableTds[16].text.strip()
    floor=mainTableTds[18].text.strip()
    allfloor=mainTableTds[20].text.strip()
    toward=mainTableTds[22].text.strip()
    deep=mainTableTds[24].text.strip()
    buildyear=mainTableTds[26].text.strip()
    size=mainTableTds[28].text.strip()
    carban=mainTableTds[30].text.strip()
    price=mainTableTds[32].find('font').text.strip()
    remark=mainTableTds[46].text.strip()

    # table2
    contactTableTds=mainTable[1].find_all('td')

    contact_name=contactTableTds[2].find('a').text.strip()
    contact_phone=contactTableTds[4].text.strip()
    phone_number=contactTableTds[6].text.strip()
    contact_qq=contactTableTds[8].text.strip()
    contact_wechat=contactTableTds[12].contents[0].strip()
    contact_address=contactTableTds[14].text.strip()

    data = {
        "info_id": qs.get('id')[0],
        "newstime":newstime,
        "origin": origin,
        "position": position,
        "name": name,
        "ftype": ftype,
        "structure": structure,
        "floor": floor,
        "allfloor": allfloor,
        "toward": toward,
        "deep": deep,
        "buildyear": buildyear,
        "size": size,
        "carban": carban,
        "price": price,
        "remark": remark,
        "contact_name": contact_name,
        "contact_phone": contact_phone,
        "phone_number": phone_number,
        "contact_qq": contact_qq,
        "contact_wechat": contact_wechat,
        "contact_address": contact_address
    }

    fc=db.fc.insert_one(data)
    return fc.inserted_id



# print(getPage('/saleshow.php?id=4080422'))

urls=db.urlcollections.find()
count=db.urlcollections.count_documents({})

for url in urls:
    u=url.get('href')
    count-=1
    print('url:%s; left: %d'%(u, count))
    getPage(u)
    sleep(1)






