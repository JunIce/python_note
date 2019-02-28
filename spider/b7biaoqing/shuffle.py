#!coding=utf-8
import random
c = open('./ext.2.txt', 'r')
a = c.read().split("\n")
random.shuffle(a)
f = open('./t2.txt', 'w+')
s = '\n'.join(a)
print(f.write(s))