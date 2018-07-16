#coding=utf-8
'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

l = '..'.join([str(x) for x in range(1000, 3000) if int(str(x)[0])%2==0 and int(str(x)[1])%2==0 and int(str(x)[2])%2==0 and int(str(x)[3])%2==0])
print(l)