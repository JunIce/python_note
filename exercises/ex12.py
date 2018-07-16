#coding
'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
dist = {'ALPHA': 0, 'DIGIT': 0}

def my(x):
  if x.isdigit():
    dist['DIGIT'] += 1
  elif x.isalpha():
    dist['ALPHA'] += 1

def calculateLetter(s):
  for x in s:
    my(x)

s = 'hello world! 123'
calculateLetter(s)
print(dist)