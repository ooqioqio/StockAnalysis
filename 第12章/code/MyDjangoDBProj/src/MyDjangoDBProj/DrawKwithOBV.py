# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl
# 计算OBV的方法 
def calOBV(df):
    # 把成交量换算成万手
    df['VolByHand'] = df['Volume']/1000000
    # 创建OBV列，先全填充为0
    df['OBV'] =0  
    cnt=1   # 索引从1开始，即从第2天算起
    while cnt<=len(df)-1:
        if(df.iloc[cnt]['Close']>df.iloc[cnt-1]['Close']):
            df.ix[cnt,'OBV'] = df.ix[cnt-1,'OBV'] + df.ix[cnt,'VolByHand']
        if(df.iloc[cnt]['Close']<df.iloc[cnt-1]['Close']):            
            df.ix[cnt,'OBV'] = df.ix[cnt-1,'OBV'] - df.ix[cnt,'VolByHand']   
        cnt=cnt+1   
    return df
filename='D:\\stockData\ch12\\6004602019-01-012019-05-31.csv'
df = pd.read_csv(filename,encoding='gbk')
# 调用方法计算OBV
df = calOBV(df) 
# print(df) # 可以去除这个注释以查看结果
figure = plt.figure()
# 创建子图     
(axPrice, axOBV) = figure.subplots(2, sharex=True)
# 调用方法，在axPrice子图中绘制K线图 
candlestick2_ochl(ax = axPrice, 
              opens=df["Open"].values, closes=df["Close"].values,
              highs=df["High"].values, lows=df["Low"].values,
              width=0.75, colorup='red', colordown='green')
axPrice.set_title("K线图和均线图")    # 设置子图标题
df['Close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均线')
df['Close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均线')
df['Close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均线')
axPrice.legend(loc='best')      # 绘制图例
axPrice.set_ylabel("价格（单位：元）")
axPrice.grid(linestyle='-.')    # 带网格线        
# 在axOBV子图中绘制OBV图形
df['OBV'].plot(ax=axOBV,color="blue",label='OBV')
plt.legend(loc='best')          # 绘制图例
plt.rcParams['font.sans-serif']=['SimHei']
# 在OBV子图上加上负值效果
plt.rcParams['axes.unicode_minus'] = False
axOBV.set_ylabel("单位：万手")
axOBV.set_title("OBV指标图")    # 设置子图的标题
axOBV.grid(linestyle='-.')      # 带网格线
# 设置x轴坐标的标签和旋转角度
major_index=df.index[df.index%5==0]
major_xtics=df['Date'][df.index%5==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.show()