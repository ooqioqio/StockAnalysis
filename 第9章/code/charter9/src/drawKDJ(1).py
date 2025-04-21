# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
# 计算KDJ
def calKDJ(df):
    df['MinLow'] = df['Low'].rolling(9, min_periods=9).min()
    # 填充NaN数据
    df['MinLow'].fillna(value = df['Low'].expanding().min(), inplace = True) 
    df['MaxHigh'] = df['High'].rolling(9, min_periods=9).max()
    df['MaxHigh'].fillna(value = df['High'].expanding().max(), inplace = True)    
    df['RSV'] = (df['Close'] - df['MinLow']) / (df['MaxHigh'] - df['MinLow']) * 100
    # 通过for循环依次计算每个交易日的KDJ值
    for i in range(len(df)):
        if i==0:    # 第一天
            df.ix[i,'K']=50
            df.ix[i,'D']=50
        if i>0:
            df.ix[i,'K']=df.ix[i-1,'K']*2/3 + 1/3*df.ix[i,'RSV']
            df.ix[i,'D']=df.ix[i-1,'D']*2/3 + 1/3*df.ix[i,'K']            
        df.ix[i,'J']=3*df.ix[i,'K']-2*df.ix[i,'D']  
    return df
# 绘制KDJ线
def drawKDJ():
    df = pd.read_csv('D:/stockData/ch8/6035052018-09-012019-05-31.csv',encoding='gbk')
    stockDataFrame = calKDJ(df)
    print(stockDataFrame)
    # 开始绘图
    plt.figure()
    stockDataFrame['K'].plot(color="blue",label='K')
    stockDataFrame['D'].plot(color="green",label='D')
    stockDataFrame['J'].plot(color="purple",label='J')
    plt.legend(loc='best') #绘制图例       
    # 设置x轴坐标的标签和旋转角度
    major_index=stockDataFrame.index[stockDataFrame.index%10==0]
    major_xtics=stockDataFrame['Date'][stockDataFrame.index%10==0]
    plt.xticks(major_index,major_xtics)
    plt.setp(plt.gca().get_xticklabels(), rotation=30) 
    # 带网格线，且设置了网格样式
    plt.grid(linestyle='-.') 
    plt.title("金石资源的KDJ图")
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.show()
# 调用方法
drawKDJ()