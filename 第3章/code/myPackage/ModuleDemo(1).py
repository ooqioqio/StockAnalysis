# !/usr/bin/env python
# coding=utf-8
def displayModuleName():
    print("CalModule")
def add(x,y):
    return x+y
def minus(x,y):
    return x-y

PI = 3.14

class Stock:
    def __init__(self, stockCode,price):
        self.stockCode, self.price = stockCode,price
    def buy(self):
        print("Buy " + self.stockCode + " with the price:" + self.price)