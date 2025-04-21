# !/usr/bin/env python
# coding=utf-8
import pandas_datareader
import pandas as pd
import numpy as np
# 涨幅是否大于指定比率
def isMoreThanPer(lessVal,highVal,per):
    if np.abs(highVal-lessVal)/lessVal>per/100:
        return True
    else:
        return False        
# 涨幅是否小于指定比率
def isLessThanPer(lessVal,highVal,per):
    if np.abs(highVal-lessVal)/lessVal<per/100:
        return True
    else:
        return False
code='600895.ss'
stock = pandas_datareader.get_data_yahoo(code,'2018-09-01','2018-12-31')
# 删除最后一行，因为get_data_yahoo会多取一天的股票交易数据
stock.drop(stock.index[len(stock)-1],inplace=True)
# 保存在本地
stock.to_csv('D:\\stockData\ch7\\60089520181231.csv')
# 从文件中读取数据
df = pd.read_csv('D:/stockData/ch7/60089520181231.csv',encoding='gbk')
cnt=0    
while cnt<=len(df)-1:
    try:
        # 规则1：连续三天收盘价变动不超过3%
        if isLessThanPer(df.iloc[cnt]['Close'],df.iloc[cnt+1]['Close'],3) and isLessThanPer(df.iloc[cnt]['Close'],df.iloc[cnt+2]['Close'],3) :
            # 规则2：连续三天成交量涨幅超过75%
            if isMoreThanPer(df.iloc[cnt]['Volume'],df.iloc[cnt+1]['Volume'],75) and isMoreThanPer(df.iloc[cnt]['Volume'],df.iloc[cnt+2]['Volume'],75) :
                print("Buy Point on:" + df.iloc[cnt]['Date'])
    except: 
        pass                
    cnt=cnt+1