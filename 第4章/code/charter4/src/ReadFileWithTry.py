# !/usr/bin/env python
# coding=utf-8
try:
    #filename = 'c:\\1\\python1.txt'
    filename = 'c:\\1\\python.txt'
    f = open(filename,'r')
    line = f.readline()               
    while line: 
        print(line, end='')    
        line = f.readline()
except:
    print("Error when handling the file:" + filename)
finally:
    try:            
        f.close()
    except:
        print("No Need to close file:" + filename) 