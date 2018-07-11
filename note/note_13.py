#!/usr/bin/python
#coding=utf-8
'''
异常和 文件处理
  通过使用 try...except 块来实 现。

Error
  (1) 使用不存在的字典关键字将引发 KeyError 异常。
  (2) 搜索列表中不存在的值将引发 ValueError 异常。
  (3) 调用不存在的方法将引发 AttributeError 异常。
  (4) 引用不存在的变量将引发 NameError 异常。
  (5) 未强制转换就混用数据类型将引发 TypeError 异常。
'''
try:
  f = open('note/open.txt', 'r')
  print(f.read())
except FileNotFoundError:
  print("File not find")