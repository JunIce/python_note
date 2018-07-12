#!/usr/bin/python
#coding=utf-8
import threading,time

lock = threading.Lock()

def sayNum(n):
  print(n)
  time.sleep(3)

def run_thread(n):
  lock.acquire()
  try:
    sayNum(n)
  finally:
    lock.release()

if __name__ == '__main__':
  t1 = threading.Thread(target=run_thread, args=(5,))
  t2 = threading.Thread(target=run_thread, args=(8,))
  t1.start()
  t2.start()
  t1.join()
  t2.join()