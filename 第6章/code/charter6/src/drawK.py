# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl  
# 从文件中获取数据
df = pd.read_csv('D:/stockData/ch6/600895.csv',encoding='gbk',index_col=0)
# 设置图的位置
fig = plt.figure()
ax = fig.add_subplot(111)
# 调用方法绘制K线图 
candlestick2_ochl(ax = ax, 
                  opens=df["Open"].values, closes=df["Close"].values,
                  highs=df["High"].values, lows=df["Low"].values,
                  width=0.75, colorup='red', colordown='green')
# 设置x轴的标签 
plt.xticks(range(len(df.index.values)),df.index.values,rotation=30 ) 
ax.grid(True) # 带网格线
plt.title("600895张江高科的K线图")
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.show()