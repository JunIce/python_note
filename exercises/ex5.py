#coding=utf-8

class Meord():
  def __init__(self):
    self.__str = ''
  def getString(self):
    self.__str = str(input())
  def printString(self):
    return self.__str.capitalize()

d = Meord()
d.getString()
s = d.printString()
print(s)