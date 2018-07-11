#!/usr/bin/python
#coding=utf-8
'''
Type
  (1) type 可以接收任何东西作为参数――我的意思是任何东西――并返回它的 数据类型。整型、字符串、列表、字典、元组、函数、类、模块，甚至类 型对象都可以作为参数被 type 函数接受。
  (2) type 可以接收变量作为参数，并返回它的数据类型。
  (3) type 还可以作用于模块。
  (4) 你可以使用 types 模块中的常量来进行对象类型的比较。这就是 info 函数所做的，很快你就会看到。
dir
  dir 函数返回任意对象的属性和方法列表
  列表只包含了字符串形式的方法名称
callable
  方法用来检测对象是否可被调用，可被调用指的是对象能否使用()括号的方法调用
  可调用对象，在实际调用也可能调用失败；但是不可调用对象，调用肯定不成功。
  类对象都是可被调用对象，类的实例对象是否可调用对象，取决于类是否定义了__call__方法。
getattr
  (1) 该语句获取列表的 pop 方法的引用。注意该语句并不是调用 pop 方法;调 用 pop 方法的应该是 li.pop()。这里指的是方法对象本身。
  (2) 该语句也是返回 pop 方法的引用，但是此时，方法名称是作为一个字符串 参数传递给 getattr 函数的。getattr 是一个有用到令人无法致信的内置函数， 可以返回任何对象的任何属性。在这个例子中，对象是一个 list，属性是 pop 方法。
  (3) 如果不确信它是多么的有用，试试这个:getattr 的返回值是 方法，然后你 就可以调用它，就像直接使用 li.append("Moe") 一样。但是实际上你没有直 接调用函数;只是以字符串形式指定了函数名称。
  (4) getattr 也可以作用于字典。
  (5) 理论上，getattr 可以作用于元组，但是由于元组没有方法，所以不管你指 定什么属性名称 getattr 都会引发一个异常。

  getattr 常见的使用模式是作为一个分发者。如果你有一个程序可以 以不同的格式输出数据，你可以为每种输出格式定义各自的格式输出函数， 然后使用唯一的分发函数调用所需的格式输出函数。
  第三个参数是一个缺省返回值，如果第二个参数指定的属性或者方法没能 找到，则将返回这个缺省返回值。
'''

L=[]
D={}
print(type(L), type(D))
#print(dir(L)) # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__','__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#print(dir(D)) # ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

def call():
  pass

print(callable(call))

# getattr

a = [1,2,3,4]
fn = getattr(a, 'pop')
print(fn)
fn() # 函数调用
print(a) # [1，2，3]

class Formate():
  def output_1(self, str):
    print('Hello, %s'%str)
  def output_2(self, str):
    print("Hi, %s"%str)

def dout(str, formate='output_1'):
  forma = Formate()
  fn = getattr(forma, '%s'%formate) #第三个参数是一个缺省返回值，如果第二个参数指定的属性或者方法没能 找到，则将返回这个缺省返回值。
  print(fn)
  return fn(str)

dout('world', 'output_2')