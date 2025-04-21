# !/usr/bin/env python
# coding=utf-8
# 定义类
class Stock:
    def __init__(self, stockCode,price):
        self.stockCode, self.price = stockCode,price
    def get_stockCode(self):
        return self.stockCode
    def set_stockCode(self,stockCode):
        self.stockCode = stockCode
    def get_price(self):
        return self.price
    def set_price(self,price):
        self.price = price  
    def display(self):
        print("Stock code is:{}, price is:{}.".format(self.stockCode,self.price))
# 使用类
myStock = Stock("600018",50)    # 实例化一个对象myStock
myStock.display() #Stock code is:600018, price is:50.
# 更改其中的值
myStock.set_stockCode("600020")
print myStock.get_stockCode()   # 600020
myStock.set_price(60)
print myStock.get_price() #60                   