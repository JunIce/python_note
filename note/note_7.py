#!/usr/bin/python
'''
S.find(substring, [start [,end]]) #可指范围查找子串，返回索引值，否则返回-1
S.rfind(substring,[start [,end]]) #反向查找
S.index(substring,[start [,end]]) #同find，只是找不到产生ValueError异常
S.rindex(substring,[start [,end]])#同上反向查找
S.count(substring,[start [,end]]) #返回找到子串的个数

S.strip() 去处空格，回车
S.startwith（sub[,start][,end]）:判断从start到end是否以sub开头
S.endswith(substring) # 以什么结尾
S.expandstabs() # 将字符串中的'\t'转换为空格
S.lstrip() 清除字符串左边空格
S.rstrip（）：去掉字符串右边的空格
S.replace（old,[,new][,count]）:将字符串中的old子串替换为new，替换count次
S.title（）将字符串标题化（即是连续字符串的第一个字母大写，其他都是小写空格，分隔的字符串都遵循此规则）
S.zfill（width）：用'0'来填充不够的空格（是从左边开始填充）
S.center(width, filter)

isalnum() :判断s是否是数字或者字母
isspace() ：判断是否是空格
isdigit() ：判断是否都是数字组成
isalpha() ：判断是否都是由字母组成的
islower() ：判断是否都是由小写字母组成的
istitle（）：判断是否是标题形式字符串（即是连续字符串只有第一个字母大写，其他都是小写，若是有空格，则每个分隔的字符串都满足此）
isupper（）：判断是否都是由大写字母组成的


S.lowercase()
S.capitalize() #首字母大写
S.lower() #转小写
S.upper() #转大写
S.swapcase() #大小写互换

S.split(str, ' ') #将string转list，以空格切分
S.join(list, ' ') #将list转string，以空格连接

处理字符串的内置函数
len(S) #长度
cmp("my friend", S) #字符串比较。第一个大，返回1
max(S) #寻找字符串中最大的字符
min(S) #寻找字符串中最小的字符

string的转换

oat(S) #变成浮点数，float("1e-1") 结果为0.1
int(S) #变成整型， int("12") 结果为12
int(S,base) #变成base进制整型数，int("11",2) 结果为2
long(S) #变成长整型，
long(S,base) #变成base进制长整型，

字符串的格式化（注意其转义字符，大多如C语言的，略）
str_format % (参数列表) #参数列表是以tuple的形式定义的，即不可运行中改变
'''
s = "Hello world"

print(s[:5])
print(s.strip())
print(s.find('llo')) 
print(s.index('lo'))
print(len(s))
print(s.count('o'))
print(s.center(40, '*'))