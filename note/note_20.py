#!/usr/bin/python
#coding=utf-8
'''
python中的队列分类可分为两种：
  1.线程Queue，也就是普通的Queue
  2.进程Queue，在多线程与多进程会介绍。

  FIFO
    Queue.Queue(maxsize=0)
    FIFO即First in First Out,先进先出。Queue提供了一个基本的FIFO容器，使用方法很简单,maxsize是个整数，指明了队列中能存放的数据个数的上限。一旦达到上限，插入会导致阻塞，直到队列中的数据被消费掉。如果maxsize小于或者等于0，队列大小没有限制。
  
  LIFO
    Queue.LifoQueue(maxsize=0)
    LIFO即Last in First Out,后进先出。与栈的类似，使用也很简单,maxsize用法同上
  
  priority
    class Queue.PriorityQueue(maxsize=0)
    构造一个优先队列。maxsize用法同上。
  
  基本方法：
    Queue.Queue(maxsize=0)   FIFO， 如果maxsize小于1就表示队列长度无限
    Queue.LifoQueue(maxsize=0)   LIFO， 如果maxsize小于1就表示队列长度无限
    Queue.qsize()   返回队列的大小 
    Queue.empty()   如果队列为空，返回True,反之False 
    Queue.full()   如果队列满了，返回True,反之False
    Queue.get([block[, timeout]])   读队列，timeout等待时间 
    Queue.put(item, [block[, timeout]])   写队列，timeout等待时间 
    Queue.queue.clear()   清空队列
  
  task_done()
    意味着之前入队的一个任务已经完成。由队列的消费者线程调用。每一个get()调用得到一个任务，接下来的task_done()调用告诉队列该任务已经处理完毕。
    如果当前一个join()正在阻塞，它将在队列中的所有任务都处理完时恢复执行（即每一个由put()调用入队的任务都有一个对应的task_done()调用）。
  join()
    阻塞调用线程，直到队列中的所有任务被处理掉。
    只要有数据被加入队列，未完成的任务数就会增加。当消费者线程调用task_done()（意味着有消费者取得任务并完成任务），未完成的任务数就会减少。当未完成的任务数降到0，join()解除阻塞。
'''
# FIFO
from queue import Queue,LifoQueue,PriorityQueue

q = Queue()
for i in range(5):
  q.put(i)
while not q.empty():
  print(q.get())

# LIFO
l = LifoQueue()

for j in range(5):
  l.put(j)

while not l.empty():
  print(l.get())

# priority

class Student(object):
  
  def __init__(self, name, score):
    self.name = name
    self.score = score
  
  def __str__(self):
    return '(%s: %s)' % (self.name, self.score)
  
  __repr__ = __str__
  
  def __lt__(self, s):  # __cmp__是py2.7的函数，python3取消了
    '''
      比较函数必须返回数值，而不是布尔值
      0 为相等
    '''
    print(self,s, self.name < s.name)
    if self.score<s.score and self.name<s.name:
      return 1
    else:
      return -1
    
pr = PriorityQueue()
pr.put(Student('Tim', 99))
pr.put(Student('Bob', 88))
pr.put(Student('Alice', 88))

while not pr.empty():
  print(pr.get())