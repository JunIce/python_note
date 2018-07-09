#!/bin/bash
# -*- coding: utf-8 -*-
import sys

# 提供了一系列有关Python运行环境的变量和函数
def testSys():
  # 参数是list
  argv = sys.argv 

  filename = argv[0] # 文件名
  # argv1 = argv[1] # 第一个参数

  print(filename)
  # print(argv1)

  # 返回已经导入的模块，list
  print(sys.modules.keys()) 

  # sys.exc_info() 获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
  # sys.exit(n) 退出程序，正常退出时exit(0)
  # sys.hexversion 获取Python解释程序的版本值，16进制格式如：0x020403F0
  # sys.version 获取Python解释程序的版本信息
  # sys.maxsize 最大的Int值
  # sys.maxunicode 最大的Unicode值
  # sys.modules 返回系统导入的模块字段，key是模块名，value是模块        dict
  # sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值    list
  # sys.platform 返回操作系统平台名称
  print(sys.platform)
  print(sys.path)
  print(sys.maxsize)
  # print(sys.modules)