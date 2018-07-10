#!/bin/bash
#encoding=utf-8

'''
  (1) List 是一个用方括号包括起来的有序元素的集合。
  (2) List 可以作为以 0 下标开始的数组。任何一个非空 list 的第一个元素总是 li[0]。
  (3) 列表总是从 0 开始。

  切片 
    返回的是一个新list
    负数索引从 list 的尾部开始向前计数来存取元素。任何一个非空的 list 最 后一个元素总是 li[-1]。

  增加 -- 改变原数组
    append 向 list 的末尾追加单个元素
    insert 将单个元素插入到 list 中。数值参数是插入点的索引。请注意，list 中的元素不必唯一，现在有两个独立的元素具有 'new' 这个值，li[2] 和 li[6]。
    extend 用来连接 list。

  索引
    list.index index 在 list 中查找一个值的首次出现并返回索引值
    c in list 测试是否包含c
  
  删除
    remove 从 list 中删除一个值的首次出现。 -- 改变原数组，无返回
    pop 是一个有趣的东西。它会做两件事:删除 list 的最后一个元素，然后返回删除元素的值。 -- 改变原数组，返回该元素的值
  
  运算符
    list = list + otherlist 相当于 list.extend(otherlist)。但 + 运算符把一个新 (连接后) 的 list 作为值返回，而 extend 只修改存在的 list。也就是说，对于大型 list 来说，extend 的执行速 度要快一些。
    * 运算符可以作为一个重复器作用于 list。li = [1, 2] * 3 等同于 li = [1, 2] + [1, 2] + [1, 2]，即将三个 list 连接成一个。
  
  常用方法
    L.append(var) #追加元素
    L.insert(index,var)
    L.pop(var) #返回最后一个元素，并从list中删除之
    L.remove(var) #删除第一次出现的该元素
    L.count(var) #该元素在列表中出现的个数
    L.index(var) #该元素的位置,无则抛异常
    L.extend(list) #追加list，即合并list到L上
    L.sort() #排序, 不能包含类型不一样的元素
    L.reverse() #倒序
    L.clear()：清空列表
    L.copy()：复制列表
    L1 = L[:] clone克隆
'''
li = [1, 2, 3, 4, 5]
print(li)

print(li[-3: -1])


a = [1,2,3]
b = [4,5,6]
a.insert(2, 'sdf')
a.extend(b)
print(a)
print(b)

# index
print(a.index('sdf'))
print(5 in a)

#del
r = a.remove('sdf')
print(a, r)

s = a.pop(1) 
print(a,s)

# 运算符
d = [1,2,3]
d+=['string']
print(d)
print(d*2)

d.remove('string')
d.sort()
print(d)
d.reverse()
print(d)
print(max(d))
print(min(d))
