#coding=utf-8
'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''


def tsum(a):
  n1 = int( "%s" % a )
  n2 = int( "%s%s" % (a,a) )
  n3 = int( "%s%s%s" % (a,a,a) )
  n4 = int( "%s%s%s%s" % (a,a,a,a))
  l = (n1,n2,n3,n4)
  print(sum(l))

tsum(9)