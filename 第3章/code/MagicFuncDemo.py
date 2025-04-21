# !/usr/bin/env python
# coding=utf-8
# 定义类
class Stock:
    def __init__(self,stockCode):
        print("in __init__")
        self.stockCode = stockCode
    # 回收类的时候被触发 
    def __del__(self):
        print("In __del__")
    def __str__(self):
        print("in __str__")
        return "stockCode is: "+self.stockCode
    def __repr__(self):        
        return "stockCode is: "+self.stockCode
    def __setattr__(self, name, value): 
        print("in __setattr__")
        self.__dict__[name] = value  # 给类中的属性名分配值 
    def __getattr__(self, key):
        print("in __setattr__")  
        if key == "stockCode":
            return self.stockCode
        else:
            print("Class has no attribute '%s'" % key)
# 初始化类，并调用类里的方法
myStock = Stock("600128")       # 触发__init__和 __setattr__方法   
print(myStock)                  # 触发__str__和__repr__方法
myStock.stockCode = "600020"    # 触发__setattr__方法