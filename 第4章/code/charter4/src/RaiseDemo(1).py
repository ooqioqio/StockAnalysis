# !/usr/bin/env python
# coding=utf-8
def divide(x,y):
    if y==0:
        raise Exception('Divisor is 0')
    try:
        return x/y
    except(TypeError):
        raise Exception('Parameters Type Error')
try:
    print(divide(1,0))
except(Exception) as e:
    print(e) # 输出Divisor is 0
try:
    print(divide(1,'1'))
except(Exception) as e:
    print(e)  # 输出Parameters Type Error