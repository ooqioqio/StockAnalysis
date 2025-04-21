# !/usr/bin/env python
# coding=utf-8
# 定义一个加法的函数add
def add(x, y):
    return x + y
print(reduce(add, [1,2,3,4,5]))     # 输出15
print(reduce(add, [1,2,3,4,5],100)) # 输出115
# 定义乘法的函数
def multiply(x,y):
    return x*y
print(reduce(multiply, [1,2,3,4,5]))  # 输出120
# 定义拼接数字的函数
def combineNumber(x, y):
    return x * 10 + y
print(reduce(combineNumber, [1,2,3,4,5])) # 输出12345