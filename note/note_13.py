#!/usr/bin/python
#coding=utf-8
'''
异常和 文件处理
  通过使用 try...except 块来实 现。

Error
  (1) 使用不存在的字典关键字将引发 KeyError 异常。
  (2) 搜索列表中不存在的值将引发 ValueError 异常。
  (3) 调用不存在的方法将引发 AttributeError 异常。
  (4) 引用不存在的变量将引发 NameError 异常。
  (5) 未强制转换就混用数据类型将引发 TypeError 异常。

open 方法可以接收三个参数:文件名、模式和缓冲区参数。
  file.name
  file.mode
  file.seek() seek 方法在被打开文件中移动到另一个位置。第二个参数指 出第一个参数是什么意思:0 表示移动到一个绝对位置 (从文件起始处算 起)，1 表示移到一个相对位置 (从当前位置算起)，还有 2 表示相对于文件 尾的位置。因为我们搜索的 MP3 标记保存在文件的末尾，我们使用 2 并 且告诉文件对象从文件尾移动到 128 字节的位置。
  file.tell() tell 方法告诉你在被 打开文件中的当前位置
  file.talk() read 方法从被打开文件中读取指定个数的字节，并且返回含有读取数据的字符串。可选参数指定了读取的最大字节数
  file.close() 这样就释放掉你加在文件上 的锁 (如果有的话)，刷新被缓冲的系统还未写入的输出 (如果有的话)，并 且释放系统资源。 file.closed属性
'''
try:
  f = open('note/open.txt', 'r')
  print(f.read())
  fd = open('note/open.txt', 'a+')
  fd.write("456")
  fd.close()
  print(fd.closed)
except FileNotFoundError:
  print("File not find")