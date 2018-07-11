#!/usr/bin/python
#coding=utf-8
'''
and 和 or 的特殊性质

and
  使用 and 时，在布尔环境中从左到右演算表达式的值。
  第一个值为假即输出假
  所有值都为真，所以 and 返回最后一个真值
or
  使用 or 时，在布尔环境中从左到右演算值，就像 and 一样。如果有一个值 为真，or 立刻返回该值。
  如果所有的值都为假，or 返回最后一个假值。
and-or
  这个语法看起来类似于 C 语言中的 bool ? a : b 表达式。整个表达式从左到 右进行演算，所以先进行 and 表达式的演算。

bool ? a : b
bool and a or b = return a if bool else b
'''

# 先算9 and 4, 9为true, 值为4. 再算3 or 4, 3为true,值为：3
print( 3 or 9 and 4) # 3
# 先算3 or 9, 3为true, 值为3. 再算3 and 4, 3为true,值为：4
print( (3 or 9) and 4) #4

def work():
  return 0

fn = work and (lambda x: x**3) or (lambda x: x) # lambda 函数在 布尔环境中总是为真。(这并不意味这 lambda 函数不能返回假值。这个函数对 象的布尔值为真;它的返回值可以是任何东西。)
print(fn(4))