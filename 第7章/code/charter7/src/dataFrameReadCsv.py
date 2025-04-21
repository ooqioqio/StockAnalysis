# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
# 从文件中读取数据
df = pd.read_csv('D:/stockData/ch6/600895.csv',encoding='gbk',index_col='Date')
print(df.head(1))   # 打印第1行数据
print(df.tail(2))   # 打印最后2行的数据
print(df.index.values)      # 打印索引列（Date）数据
print(df['Close'].values)   # 打印索引列（Date）数据
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)       # 带网格线
df['Open'].plot(color="red",label='Open')#绘制开盘价 
df['Close'].plot(color="blue",label='Close')#绘制收盘价
plt.legend(loc='best')      # 绘制图例
# 设置x轴的标签
plt.xticks(range(len(df.index.values)),df.index.values,rotation=30 ) 
plt.show()