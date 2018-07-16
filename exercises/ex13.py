#coding=utf-8
'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

s = 'Hello world!'

dist = {'UPPER': 0, 'LOWER': 0}

for i in s:
  if i.isupper():
    dist['UPPER'] += 1
  elif i.islower():
    dist['LOWER'] += 1

print(dist)