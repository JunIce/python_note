#coding=utf-8
'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

def sortSenten(str):
  l = str.split(',')
  c = list(map(lambda x: x.lower(), l))
  c.sort()
  return '-'.join(c)


d = sortSenten('without,hello,bag,world')
print(d)
