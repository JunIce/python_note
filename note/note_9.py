#!/usr/bin/python
# coding=utf-8
'''
参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。

默认参数
  默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。默认参数放在必选参数后面
  *  默认参数必须指向不变对象！ 也就是默认参数不能是list https://blog.csdn.net/u014680098/article/details/70231775

可变参数
  定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
  Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

关键字参数
  关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
  它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

命名关键字参数 -- py2.7没有此项功能 python3才可以使用
  命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。 # def person(name, age, *, city='Beijing', job):
  使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数。


总结
  Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
  默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
  要注意定义可变参数和关键字参数的语法：
    *args是可变参数，args接收的是一个tuple；
    **kw是关键字参数，kw接收的是一个dict。

  以及调用函数时如何传入可变参数和关键字参数的语法：
    可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
    命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
    定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。
'''



# 默认参数
def defaultParam(a, x=10):
  return a * 2 + x

print(defaultParam(6))

def defaultPara(la = []):
  la.append(1)
  return la

print(defaultPara()) # [1]
print(defaultPara()) # [1,1]

# 可变参数
def summ(*args):
  total = 0
  for n in args:
    total += int(n)
  return total

print(summ(1,2,3))
print(summ(*[1,2,3])) # list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去


# 关键字参数
def keyWordParams(name, age, **kw):
  return { 'name': name, 'age': age, 'data': kw}

data = { 'sex': 'female', 'company': 'Alibaba'}
print(keyWordParams('Jack', 30, job='enginer', address='PuShan Road'))
print(keyWordParams('Ma', 50, **data)) # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数
def defineKeyWordParam(name, age, *, sex, **kw):
  return { 'name': name, 'age': age, 'sex': sex,'data': kw}

print(defineKeyWordParam('Jack', 30, sex='male', job='enginer', address='PuShan Road'))