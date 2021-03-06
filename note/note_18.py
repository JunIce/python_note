#!/usr/bin/python
#coding=utf-8
'''
HTTP
  User-Agent 
    是一种客户端告知服务器谁在什么时候通过 HTTP 请求了一个 web 页、feed 汇聚或其他类型的 web 服务的简单途径。当客户端请求一个资源时， 应该尽可能明确发起请求的是谁，以便当产生异常错误时，允许服务器端的 管理员与客户端的开发者取得联系。
  Redirects 
    HTTP 有两种不同的方法表示资源已经被移动。状态代码 302 表示临时重定向;状态代码 301 表示永久重定向;
  Last-Modified/If-Modified-Since
    所有现代的浏览器都支持最近修改 (last-modified) 的数据检查。如果你曾经访 问过某页，一天后重新访问相同的页时发现它没有变化，并奇怪第二次访问 时页面加载得如此之快——这就是原因所在。你的浏览器首次访问时会在本 地缓存页面内容，当你第二次访问，浏览器自动发送首次访问时从服务器获 得的最近修改日期
  ETag/If-None-Match
    ETag 是实现与最近修改数据检查同样的功能的另一种方法:没有变化时不重 新下载数据。其工作方式是:服务器发送你所请求的数据的同时，发送某种 数据的 hash (在 ETag 头信息中给出)。
  Compression
    Python 的 URL 库本身没有内置对 gzip 压缩的支持，但是你能为请求添加任意 的头信息。Python 还提供了一个独立的 gzip 模块，它提供了对数据进行解压 缩的功能。
'''

