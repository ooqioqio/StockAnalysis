# !/usr/bin/env python
# coding=utf-8
def divide(x,y):
    try:
        return x/y
    except(ZeroDivisionError, TypeError, Exception) as e:
        print(e) 
# 如下是各种错误的调用       
print(divide(1,'1'))    # 触发TypeError异常
print(divide(1,0))      # 触发ZeroDivisionError