#coding=utf-8
import time
import multiprocessing

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
def noprocess():
  fib(35)
  fib(35)

@log
def hasProcess():
  p = []
  for i in range(2):
    t = multiprocessing.Process(target=fib, args=(35,))
    t.start()
    p.append(t)
  
  
  for th in p:
    th.join()



noprocess()
hasProcess()