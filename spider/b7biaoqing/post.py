#!/usr/bin/python
#coding=utf-8
import requests
import time
from requests.cookies import RequestsCookieJar

c = open('./t2.txt', 'r')
url = "https://www.woyaogexing.com/e/DoInfo/ecms.php"
classid = 110
mid = 19
cookie_jar = RequestsCookieJar()
cookie_jar.set('gqbcemluserid', '421823')
cookie_jar.set('gqbcemlusername', '%E3%81%96%E5%86%BB%E7%BB%93%E3%81%AE%E2%86%92%E7%88%B1')
cookie_jar.set('gqbcemlrnd', 'UNlz1y1CeFrpKMJ8gc9s')
cookie_jar.set('gqbcemlgroupid', '2')

def pathDir(p):
    # return '/d/file/2019/01/05/{}'.format(p)
    return 'https://img2.woyaogexing.com/2019/01/08/{}'.format(p)
count = 1
for line in c:
    lines = [v for v in line.replace("\n","").split('----')]
    print(lines)
    data = {
        'enews': 'MAddInfo',
        'zt_ids': [],
        'classid' : classid,
        'mid': mid,
        'title': lines[2],
        'titlepic': pathDir(lines[1]),
        'newstext': '<p align="center"><img src="{}" /></p>'.format(pathDir(lines[0]))
    }
    c = requests.post(url, data=data, cookies=cookie_jar)
    time.sleep(1)
    count += 1
    print(count)

