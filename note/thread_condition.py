#!/usr/bin/python
#coding=utf-8
import threading,time

def Buyer(cond):
  cond.acquire()
  for i in range(3):
    print("I'm buying !!!")
    time.sleep(2)
  print("Buying end")
  cond.notify()
  cond.wait()
  print("Hei, this is %d dollars"% 100)
  cond.notify()
  cond.release()


def Seller(cond):
  cond.acquire()
  print("i get it")
  for i in range(3):
    print("calculating the total price")
    time.sleep(2)
  print("Total price is %d"% 100)
  cond.notify()
  cond.wait()
  print("Thanks!!")
  cond.release()



if __name__ == '__main__':
  cond = threading.Condition()
  buyer = threading.Thread(target=Buyer, args=(cond,))
  seller = threading.Thread(target=Seller, args=(cond,))
  buyer.start()
  seller.start()
  buyer.join()
  seller.join()

