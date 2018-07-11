#!/usr/bin/python
#coding=utf-8
'''
locals and globals
当一行代码要使用变量 x 的值时，Python会到所有可用的名字空间去查找变量，按照如下顺序：

  1.局部名字空间 - 特指当前函数或类的方法。如果函数定义了一个局部变量 x，Python将使用这个变量，然后停止搜索。
  2.全局名字空间 - 特指当前的模块。如果模块定义了一个名为 x 的变量，函数或类，Python将使用这个变量然后停止搜索。
  3.内置名字空间 - 对每个模块都是全局的。作为最后的尝试，Python将假设 x 是内置函数或变量。

from module import 和 import module之间的不同。
  使用 import module，模块自身被导入，但是它保持着自已的名字空间，这就是为什么你需要使用模块名来访问它的函数或属性（module.function）的原因。
  但是使用 from module import，实际上是从另一个模块中将指定的函数和属性导入到你自己的名字空间，这就是为什么你可以直接访问它们却不需要引用它们所来源的模块的原因。

locals 是只读的，globals 不是
'''


def foo(arg, a):
	x = 1
	y = 'xxxxxx'
	for i in range(10):
		j = 1
		k = i
	print locals()
 
 
foo(1,2) #{'a': 2, 'i': 9, 'k': 9, 'j': 1, 'arg': 1, 'y': 'xxxxxx', 'x': 1}
