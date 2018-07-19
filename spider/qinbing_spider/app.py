#coding=utf-8
from threading import Thread
from queue import Queue
from multiprocessing import Pool
import time
from main_process import MainProcess




if __name__ == '__main__':
  q = Queue()
  d = MainProcess(q)
  # d.go()
  d.doContents()