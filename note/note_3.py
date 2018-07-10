#!/bin/bash
# coding: utf-8


'''
    Dictionary 
    (1) 在一个 dictionary 中不能有重复的 key。给一个存在的 key 赋值会覆盖原 有的值。
    (2) 在任何时候都可以加入新的 key-value 对。这种语法同修改存在的值是一 样的
    (3) Dictionary 是无序的, key 是大小写敏感的
    (4) Dictionary 不只是用于存储字符串。Dictionary 的值可以是任意数据类型， 包括字符串、整数、对象，甚至其它的 dictionary。在单个 dictionary 里， dictionary 的值并不需要全都是同一数据类型，可以根据需要混用和匹配。
    (5) Dictionary 的 key 要严格多了，但是它们可以是字符串、整数或几种其它 的类型 (后面还会谈到这一点)。也可以在一个 dictionary 中混用和匹配 key 的数据类型。
    (6) clear 从一个 dictionary 中清除所有元素。

    常用方法：
      D.get(key, 0) #同dict[key]，多了个没有则返回缺省值，0。[]没有则抛异常
      D.has_key(key) #有该键返回TRUE，否则FALSE  python3 废弃 ， 2.7
      D.keys() #返回字典键的列表
      D.values()
      D.items()

      D.update(dict2) #增加合并字典
      D.popitem() #得到一个pair，并从字典中删除它。已空则抛异常
      D.clear() #清空字典，同del dict
      D.copy() #拷贝字典
      D.cmp(dict1,dict2) #比较字典，(优先级为元素个数、键大小、键值大小)
''' 

d = { 'a': 'string', '1': [1,2,3], 'string':(1,2,3), '321': '11'}

del d['321']

# del
print(d)

# pop
print(d.pop('a'))

#d.clear()
#print(d)

dict = {'Name': 'Runoob', 'Age': 7, 'string': (1,2,3)}

print(dict.get('1'))
#print(dict.has_key(1))
print(dict.values())
print(dict.keys())
print(dict.items())


# dict 按键排序
tmp = sorted(dict.items(), key=lambda x: x[0])
print(tmp)

