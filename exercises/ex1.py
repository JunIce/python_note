#coding=utf-8
'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
编写一个程序，找出所有这些能被7整除但不是5的倍数的数，
在2000年到3200年之间(都包括在内)。
获得的数字应该以逗号分隔的序列打印在一行上。
'''

def main():
  m,n = 2000,3200
  L =[]
  
  # 1)
  # for i in range(m,n):
  #   if i%7==0 and i%5!=0:
  #     L.append(str(i))
  

  # 2)
  L = [str(x) for x in range(m,n) if x%7==0 and x%5!=0]
  return ','.join(L)

if __name__ == '__main__':
  s = main()
  print(s)