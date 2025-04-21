# !/usr/bin/env python
# coding=utf-8
from wsgiref.simple_server import make_server
def myWebApp(environ, response):
    response('200 OK', [('Content-Type', 'text/html')])
    return ['Web Page Created by WSGI.'.encode(encoding='utf_8')]

# 创建一个服务器，端口是8080，用于处理的方法是myWebApp
httpd = make_server('localhost', 8080, myWebApp)
print("Starting HTTP Server on 8080...")
# 监听HTTP请求，如果有请求，则调用myWebApp方法进行处理
httpd.serve_forever()