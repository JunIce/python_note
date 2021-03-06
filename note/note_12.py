#!/usr/bin/python
#coding=utf-8
import time
'''
  1. 类名通常是第一个字母大写
  2. 这个类没有定义任何方法或属性，但是从语法上，需要在定义中有些东西， 所以你使用 pass。这是一个 Python 保留字，仅仅表示 “向前走，不要往这 看”。它是一条什么都不做的语句，当你删空函数或类时，它是一个很好 的占位符。
  3. 你可能猜到了，在类中的所有东西都要缩近，就像位于函数、if 语句，for 循环，诸如此类的代码。第一条不缩近的东西不属于这个类。
  4. __init__ 在类的实例创建后被立即调用。注意 __init__ 方法从不返回一个值。
  5. 每个类方法的第一个参数，包括 __init__，都是指向类的当前实例的引用。 按照习惯这个参数总是被称为 self。在 __init__ 方法中，self 指向新创建的 对象;在其它的类方法中，它指向方法被调用的类实例。尽管当定义方法 时你需要明确指定 self，但在调用方法时，你不 用指定它，Python 会替你 自动加上的。
  6. Python 支持数据属性,它是由某个特定的类实例所拥有的数据。

  7. __getitem__ 它只 是重定向到字典，返回字典的值。
  8.__setitem__ 简单地重定向到真正的字典 self.data 
  9. __repr__ 是一个专用的方法，在当调用 repr(instance) 时被调用。repr 函数是 一个内置函数，它返回一个对象的字符串表示。它可以用在任何对象上， 不仅仅是类的实例。
  10. __cmp__ 在比较类实例时被调用。通常，你可以通过使用 == 比较任意两个 Python 对象，不只是类实例。有一些规则，定义了何时内置数据类型被认 为是相等的，例如，字典在有着全部相同的关键字和值时是相等的。对于 类实例，你可以定义 __cmp__ 方法，自已编写比较逻辑，然后你可以使用 == 来比较你的类，Python 将会替你调用你的 __cmp__ 专用方法。
  11. __len__ 在调用 len(instance) 时被调用。len 是一个内置函数，可以返回一个对象的长度。它可以用于任何被认为理应有长度的对象。字符串的 len 是 它的字符个数;字典的 len 是它的关键字的个数;列表或序列的 len 是元 素的个数。对于类实例，定义 __len__ 方法，接着自已编写长度的计算，然 后调用 len(instance)，Python 将替你调用你的 __len__ 专用方法。
  12. __delitem__ 在调用 del instance[key] 时调用 ，你可能记得它作为从字典中删 除单个元素的方法。当你在类实例中使用 del 时，Python 替你调用 __delitem__ 专用方法。

'''
class Human():
  eyes = 2
  legs = 2

m = Human()
print(type(m))
print(type(Human))
print(m.__class__) # 引用该对象，由该对象里面的__class__找到该类

'''
1.类属性和实例属性
  1）类属性：定义在类中且在函数体之外，可以通过类名访问其属性；类属性被对应的各个实例中共享；类属性通常不作为实例属性使用
  2）实例属性：定义在方法中的属性，只作用于当前实例的类
  3）类对象的__dict__属性（只读属性）默认不能被赋值修改，可以通过setattr方法修改；而一般对象里面的__dict__属性能被直接修改
  4）一般情况下，属性存储在__dict__的字典中，有些内置对象没有这个__dict__属性
  5）能通过实例找到类属性，不能通过类访问实例属性
  6）变量后面加_:表示与系统关键字进行区分的命名方式；变量后面加__:表示系统内置的写法
  7）实例属性访问机制：getattribute方法---调用描述器方法的get方法---实例自身的dict字典---对应类的dict字典---父类(上层)的dict字典---调用getattr方法
  8) 限制实例属性的添加__slots__ , 以list方式储存

类属性
  __dict__ 类属性
  __bases__ 类的父类构成的tuple
  __doc__ 类文档字符串
  __name__ 类名
  __module__ 类定义所在的模块
实例属性
  __dict__ 实例属性
  __class__ 实例对应的类

'''
print(Human.__dict__)
print(Human.__module__)
print('line'.center(100,'-'))
class Fa():
  pass
class So(Fa):
  __slots__ = ('age')
  pass

x = So()
x.age = 30
x.address = 'nj'
print(x.__dict__)

'''
公有属性、受保护属性、私有属性

（1）公有属性：共享的属性，一般的属性
（2）受保护属性：受到保护的属性，用 _ 前缀表示
（3）私有属性：防止外界直接访问，防止被子类同名称属性覆盖，进行数据保护和数据过滤，用 __ 前缀表示，实例不能访问私有属性
'''
print('line'.center(100,'-'))
class Test():
  ob = 2
  _prot = 'jack'
  __sdcard = 'sdcard'

  @property
  def card(self):
    return self.__sdcard

t = Test()
print(t.ob, t._prot)
print(t.card)

'''
静态方法和类方法
  1) staticmethod和classmethod被引入，用来转化类中某一方法为这两种方法之一
  2) 静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，主要是一些逻辑属于类，但是和类本身没有交互，即在静态方法中，不会涉及到类中的方法和属性的操作。可以理解为将静态方法存在此类的名称空间中。事实上，在python引入静态方法之前，通常是在全局名称空间中创建函数。
'''
print('line'.center(100,'-'))

class Time():

  @staticmethod # 如果方法只通过类调用，而不需要通过实例调用的话，不用非要声明为静态的。 python3
  def showTime():
    return time.strftime("%H:%M:%S", time.localtime())

  @classmethod
  def nowTime():
    return 123
print(Time.showTime())