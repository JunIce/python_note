#coding=utf-8
'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
编写一个程序来计算给定数字的阶乘。
结果应该以逗号分隔的序列打印在一行上。
假设以下输入被提供给程序:8
然后，输出应该是:
40320
'''

def fact(x):
  if(x == 0):
    return 1
  return x*fact(x-1)

print(fact(8))