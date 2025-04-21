# !/usr/bin/env python
# coding=utf-8
from wsgiref.simple_server import make_server
def myWebApp(environ, response):
    response('200 OK', [('Content-Type', 'text/html')])
    method = environ['REQUEST_METHOD']
    param = environ['PATH_INFO'][1:]
    if method=='GET':        
        body='WSGI Get Demo!' + param
    return [body.encode(encoding='utf_8')]

httpd = make_server('localhost', 8080, myWebApp)
print("Starting HTTP Server on 8080...")
httpd.serve_forever()