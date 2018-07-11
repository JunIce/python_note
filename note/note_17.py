#!/usr/bin/python
#coding=utf-8
'''
python xml解析

minidom
  minidom.parse(filename)    #加载读取XML文件
  doc.documentElement        #获取XML文档对象
  node.getAttribute(AttributeName)    #获取XML节点属性值
  node.getElementsByTagName(TagName)    #获取XML节点对象集合
  node.childNodes    #返回子节点列表。
  node.childNodes[index].nodeValue    #获取XML节点值
  node.firstChild    #访问第一个节点。等价于pagexml.childNodes[0]
  doc = minidom.parse(filename)
  doc.toxml('UTF-8')    #返回Node节点的xml表示的文本
  Node.attributes["id"]    #访问元素属性
  a.name    #就是上面的 "id"
  a.value    #属性的值

*使用parse()或createDocument()返回的为DOM对象；
*使用DOM的documentElement属性可以获得Root Element;
*DOM为树形结构，包含许多的nodes，其中element是node的一种，可以包含子elements，textNode也是node的一种，是最终的子节点；
*每个node都有nodeName，nodeValue，nodeType属性，nodeValue是结点的值，只对textNode有效。对于textNode，想得到它的文本内容可以使用: .data属性。
'''
from xml.dom import minidom
dom = minidom.parse('note/test.xml')
nodes = dom.getElementsByTagName('T1348647853363')[0].childNodes
for node in nodes:
  if node.nodeName == 'e':
    n = node.getElementsByTagName('boardid')[0]
    print(n.childNodes[0].data) # 获取元素文本值
