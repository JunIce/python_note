#coding=utf-8
import time
import threading

def log(fn):
  def wrapper(*args, **kwargs):
    import time
    start = time.time()
    fn(*args, **kwargs)
    end = time.time()
    print('time-cost: %ds'%(end-start))
  return wrapper

def fib(n):
  if n <=2:
    return 1
  return fib(n-1) + fib(n-2)

@log
def nothread():
  fib(35)
  fib(35)

@log
def hasThread():
  for i in range(2):
    t = threading.Thread(target=fib, args=(35,))
    t.start()
  
  main_thread = threading.currentThread()
  for th in threading.enumerate():
    if th is main_thread:
      continue
    th.join()



nothread()
hasThread()