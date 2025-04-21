# !/usr/bin/env python
# coding=utf-8
stockInfoList = ['600001','600002']
try:
    print(stockInfoList[4]) # 索引出错时会触发
    # 1/0
except IndexError: 
    print('Index Error')    
try:
    # 参数的值正确，但返回值不符合预期时会触发 
    print(stockInfoList.index('600003'))    
except ValueError: 
    print('Value Error')
try:
    2+'error'   # 函数参数类型不正确时会触发
except TypeError: 
    print('Type Error')
try:
    1/0 # 除零异常
except ZeroDivisionError: 
    print('ZeroDivision Error')
class Car:       
    def __init__(self,owner):
        self.owner = owner      
myCar = Car("Peter")
try:
    print(myCar.price)  # 引用属性错误时触发
except AttributeError: 
    print('Attribute Error')