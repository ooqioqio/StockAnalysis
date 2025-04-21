# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
# 计算RSI的方法，输入参数periodList传入周期列表 
def calRSI(df,periodList):
    # 计算和上一个交易日收盘价的差值
    df['diff'] = df["Close"]-df["Close"].shift(1) 
    df['diff'].fillna(0, inplace = True)    
    df['up'] = df['diff']
    # 过滤掉小于0的值
    df['up'][df['up']<0] = 0
    df['down'] = df['diff']
    # 过滤掉大于0的值
    df['down'][df['down']>0] = 0
    # 通过for循环，依次计算periodList中不同周期的RSI等值
    for period in periodList:
        df['upAvg'+str(period)] = df['up'].rolling(period).sum()/period
        df['upAvg'+str(period)].fillna(0, inplace = True)
        df['downAvg'+str(period)] = abs(df['down'].rolling(period).sum()/period)
        df['downAvg'+str(period)].fillna(0, inplace = True)
        df['RSI'+str(period)] = 100 - 100/((df['upAvg'+str(period)]/df['downAvg'+str(period)]+1))
    return df
filename='D:\\stockData\ch10\\6005842018-09-012019-05-31.csv'
df = pd.read_csv(filename,encoding='gbk')
list = [6,12,24]    # 周期列表
# 调用方法计算RSI
stockDataFrame = calRSI(df,list) 
print(stockDataFrame)
# 开始绘图
plt.figure()
stockDataFrame['RSI6'].plot(color="blue",label='RSI6')
stockDataFrame['RSI12'].plot(color="green",label='RSI12')
stockDataFrame['RSI24'].plot(color="purple",label='RSI24')
plt.legend(loc='best')  # 绘制图例       
# 设置x轴坐标的标签和旋转角度
major_index=stockDataFrame.index[stockDataFrame.index%10==0]
major_xtics=stockDataFrame['Date'][stockDataFrame.index%10==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
# 带网格线，且设置了网格样式
plt.grid(linestyle='-.') 
plt.title("RSI效果图")
plt.rcParams['font.sans-serif']=['SimHei']
plt.savefig('D:\\stockData\ch10\\6005842018-09-012019-05-31.png')
plt.show()

