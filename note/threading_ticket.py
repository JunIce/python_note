#!/usr/bin/python
#coding=utf-8
#__auther__='east_qiu'

import threading
import time,os

def seal_ticket(s):
  global i,lock
  while True:
    lock.acquire()
    if i != 0:
      i -= 1
      print('窗口：%d, 余票：%d'%(s, i))
      time.sleep(1)
    else:
      print("Thread_id",s,"No more tickets")
      os._exit(0)
    lock.release()
    time.sleep(1)

lock = threading.Lock()
i = 100

def main():
  threads = []
  for i in range(5):
    thread = threading.Thread(target=seal_ticket, args=(i,))
    thread.daemon = True
    thread.start()
    threads.append(thread)

if __name__ == '__main__':
  main()