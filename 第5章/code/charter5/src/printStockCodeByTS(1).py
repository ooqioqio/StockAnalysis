# coding=utf-8
import tushare as ts
stockList=ts.get_stock_basics()
for code in stockList.index:
    print(code)