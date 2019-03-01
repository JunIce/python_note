#!/usr/bin/python
#coding=utf8

import requests

from urllib import parse
from bs4 import BeautifulSoup
from pymongo import MongoClient
from time import sleep
import random
client = MongoClient(host='0.0.0.0',port=27017)
db=client.jdfc
user_agent = [                   #浏览器头部
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]

def getPage(u):
    url='http://www.jddyfw.com/%s'%u
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTZjNDNmNjgzZWY5OWQ4ZWRmNTA5MzU3YWJiOGJlYWMwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVBsU3h6aU0xa25KWlZXZE5qZ0tGd21xYkJtc3J0K2w0YlEwdUhlNjFBN009BjsARg%3D%3D--abe7f4154a205b8515bfb204e3fe924006ae1d68",
        "Host": "www.xicidaili.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agent)
    }

    proxy_dict = {
        'http': 'http://116.209.59.110:9999'
    }

    query=parse.urlsplit(url).query
    qs=parse.parse_qs(query)

    res=db.fc.find_one({'info_id': qs.get('id')[0]})
    if not (res is None):
        return

    p=requests.get(url, headers=headers, timeout=10, proxies=proxy_dict)
    p.encoding='gb2312'

    

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

urls=db.urlcollections.find().skip(11559-9890)
count=db.urlcollections.count_documents({})

for url in urls:
    u=url.get('href')
    count-=1
    print('url:%s; left: %d'%(u, count))
    getPage(u)
    sleep(1)






