#!/usr/bin/python
#coding=utf-8
'''
将一个 tuple 赋值给另一个 tuple，会按顺序将 元组 的每个值赋值给每个变量。
内置的 range 函数返回一个元素为整数的 list。

字符串格式化
  %f 格式符选项对应一个十进制浮点数，不指定精度时打印 6 位小数。
  使用包含“.2”精度修正符的 %f 格式符选项将只打印 2 位小数。

映射List

'''
print("Today's stock price: %.2f" % 50.4625)
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

print(params.items())
l = [k for k,v in params.items()]
print(l)
s = ','.join(l)
print(s)

# 练习string
print(s.split(','))