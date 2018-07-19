#coding=utf-8
import redis

class RdsPool():
  def __init__(self):
    self._pool = redis.ConnectionPool(host='127.0.0.1',port=6579)
    self._conn = redis.Redis(connection_pool=self._pool)
  
  def set(self, k ,v, time=None):
    self._conn.set(k, v, time)
  
  def get(self, k):
    return self._conn.get(k)

  def lpush(self, k, v):
    self._conn.lpush(k, v)

  def lpop(self, k):
    return self._conn.lpop(k)

  def lindex(self,k,idx):
    return self._conn.lindex(k,idx)
  

