#!/usr/bin/python
#coding=utf-8
def fib(max):
  n,a,b = 0,0,1
  while n < max:
    yield b
    print('---第%d次:a,b(%d,%d)----'%(n,a,b))
    a,b = b, a+b
    n += 1
    print('第%d次结束--------'%n)
  return 'done'

if __name__ == '__main__':
  for i in fib(10):
    print(i)