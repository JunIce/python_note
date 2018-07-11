#!/usr/bin/python
#coding=utf-8

'''
正则表达式
  Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。




.	    代表任意字符
|	    逻辑或操作符
[ ]	  匹配内部的任一字符或子表达式
[^]	  对字符集和取非
-	    定义一个区间
\	    对下一字符取非（通常是普通变特殊，特殊变普通）
*	    匹配前面的字符或者子表达式0次或多次
*?	  惰性匹配上一个
+	    匹配前一个字符或子表达式一次或多次
+?	  惰性匹配上一个
?	    匹配前一个字符或子表达式0次或1次重复
{n}	  匹配前一个字符或子表达式
{m,n}	匹配前一个字符或子表达式至少m次至多n次
{n,}	匹配前一个字符或者子表达式至少n次
{n,}?	前一个的惰性匹配
^	    匹配字符串的开头
\A	  匹配字符串开头
$	    匹配字符串结束
[\b]	退格字符
\c	  匹配一个控制字符
\d	  匹配任意数字
\D	  匹配数字以外的字符
\t	  匹配制表符
\w	  匹配任意数字字母下划线
\W	  不匹配数字字母下划线
'''

import re
'''
re.match(pattern, string, flags=0)	  从字符串的起始位置匹配，如果起始位置匹配不成功的话，match()就返回none 只要找到第一个匹配然后返回
re.search(pattern, string, flags=0)	  扫描整个字符串并返回第一个成功的匹配
re.findall(pattern, string, flags=0)	找到RE匹配的所有字符串，并把他们作为一个列表返回
re.finditer(pattern, string, flags=0)	找到RE匹配的所有字符串，并把他们作为一个迭代器返回
re.sub(pattern, repl, string, count=0, flags=0)	替换匹配到的字符串
re.split(pattern, string)；将字符串按空格分割成一个单词列表。
re.subn(pattern, repl, string, count=0, flags=0) 返回替换次数

  match和search一旦匹配成功，就是一个match object对象，而match object对象有以下方法：
    group() 返回被 RE 匹配的字符串
    start() 返回匹配开始的位置
    end() 返回匹配结束的位置
    span() 返回一个元组包含匹配 (开始,结束) 的位置
    group() 返回re整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。
'''
str='Tina is a good girl, she is cool, clever, and so on...'
pattern = re.compile(r'\w*oo\w*')
#match = pattern.search(str)
#print(match)
search = pattern.search(str)
print(search.group())


print(re.split('\d+','one1two2three3four4five5'))

print(re.sub(r'\s+', '-', str)) # 字符串替换
print(re.sub(r'\s+', lambda m:'['+m.group(0)+']', str,0)) # 字符串替换为输出函数


'''
注意点
  1、re.match与re.search与re.findall的区别：  
      re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
  2. 贪婪匹配与非贪婪匹配 
      *?,+?,??,{m,n}?    前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
'''