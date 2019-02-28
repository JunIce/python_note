#coding=utf-8
import re
import json
import codecs
from RdPool import RdsPool

redis = RdsPool()

reg = '价格|鸡蛋|价格|批发|协会|参考价|\&|：|【|】{1,}'
for i in range(100):
  value = redis.lindex('content_new_ori', i).decode('utf-8')

  print("".join(value.split()))





