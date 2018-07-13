#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
from queue import Queue


#继承一个线程类threading.Thread
class DoRun(threading.Thread):
  #结构方法，初始化属性，传入一个队列
  def __init__(self, queue):
    #继承结构方法
    threading.Thread.__init__(self)
    #两个下划线表示私有变量
    self.__queue = queue

  def run(self):
    #线程的方法run start后执行的每次都取
    while not self.__queue.empty():
      ip = self.__queue.get()
      print(ip)


def main():
  threads = []
  thread_count = 10
  queue = Queue()

  for i in range(1, 255):
    queue.put('106.42.25.' + str(i))
  for i in range(thread_count):
    threads.append(DoRun(queue))
  for i in threads:
    i.start()


if __name__ == '__main__':
  main()
