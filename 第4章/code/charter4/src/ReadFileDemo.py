# !/usr/bin/env python
# coding=utf-8
f = open("c:\\1\\python.txt",'r')
line = f.readline()               
while line: 
    print(line, end='')    
    line = f.readline()
f.close()   