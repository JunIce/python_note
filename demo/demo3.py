#!/bin/bash
# coding: utf-8

def doMath():
  '''
  题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
  x + 100 = m^2
  x + 100 + 168 = n^2
  '''
  x1 = map(lambda i:i**2-100,range(1,100))
  x2 = map(lambda i:i**2-100-168,range(1,100))

  return (set(list(x1)) & set(list(x2)))
