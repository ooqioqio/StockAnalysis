# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt  
def drawK(open,close,high,low,pos):
    if close > open:    # 收盘价比开盘价高，上涨
        myColor='red'
        myHeight=close-open
        myBottom=open
    else:               # 下跌
        myColor='green'
        myHeight=open-close
        myBottom=close    
    # 根据开盘价和收盘价绘制实体      
    plt.bar(pos, height=myHeight,bottom=myBottom, width=0.2,color=myColor)
    # 根据最高价和最低价绘制上下影线
    plt.vlines(pos, high, low, myColor)
# 定义时间范围
day = ['20190422','20190423','20190424','20190425','20190426','20190429','20190430']
drawK(10.2,10.5,9.5,11,0)       # 0422交易情况
drawK(10.5,10,10.6,9.8,1)       # 0423交易情况
drawK(10,10.7,10.9,9.9,2)       # 0424交易情况
drawK(10.7,10.1,10.9,9.9,3)     # 0425交易情况
drawK(10.1,10.2,10.5,9.5,4)     # 0426交易情况
drawK(10.2,10.8,10.8,10.1,5)    # 0429交易情况
drawK(10.8,11.5,10.8,11.1,6)    # 0430交易情况
 
plt.ylim(0,15)  # 设置y轴的取值范围
plt.xticks(range(len(day)),day) # 设置x轴的标签
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.title('xx股票K线图(20190422到20190430)')  
plt.show()  