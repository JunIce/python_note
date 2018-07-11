#!/usr/bin/python
#coding=utf-8
'''
基于 dictionary 的字符 串格式化介绍
  (1) 这种字符串格式化形式不用显式的值的 tuple，而是使用一个 dictionary，params。并且标记也不是在字符串中的一个简单 %s，而是包含 dictionary 中的一个键 字，所以 %(pwd)s 标记被替换成相应的值 secret。
  (2) 基于 dictionary 的字符串格式化可用于任意数量的有名的键字。每个键字 必须在一个给定的 dictionary 中存在，否则这个格式化操作将失败并引发 一个 KeyError 的异常。
  (3) 您甚至可以两次指定同一键字，每个键字出现之处将被同一个值所替换。
'''
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print("%(pwd)s is not a good password for %(uid)s" % params)