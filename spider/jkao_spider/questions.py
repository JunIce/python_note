#coding=utf-8
import requests
import json
import pymysql

data = {'_appName': 'jiakaobaodian', '_platform': 'wap', '_r': 113808151057482128081, 'carType': 'car', 'cityCode': 320100, 'course': 'kemu1', '_': 0.4276018024265127}
url = 'https://api2.jiakaobaodian.com/api/open/exercise/sequence.htm'
headers = {
  'Origin': 'http://m.jiakaobaodian.com',
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

db = pymysql.connect(host='127.0.0.1', port=3310, user='root', passwd='1', db='jiakao', charset='utf8mb4')
cursor = db.cursor()

def save(questionId):
  try:
    sql = "INSERT INTO `questions` (`questionId`, `type`) VALUES(%d,'%s')"%(questionId, 'kemu1')
    cursor.execute(sql)
    db.commit()
  except Exception as e:
    print('a')
    db.rollback()

r = requests.get(url, params=data, headers=headers)
data = json.loads(s=r.text)
for i in data['data']:
  save(i)
cursor.close()
db.close()
