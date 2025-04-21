# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
# 从文件中读取数据
df = pd.read_excel('D:/stockData/ch5/600895.ss.xlsx')
for index,row in df.iterrows():
    df.at[index, 'NewDate'] = df.at[index, 'Date'].strftime('%Y-%m-%d')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)           # 带网格线
df['High'].plot(color="red",label='High')   # 绘制最高价 
df['Low'].plot(color="blue",label='Low')    # 绘制最低价
plt.legend(loc='best')  # 绘制图例
# 设置x轴的标签
plt.xticks(range(len(df['NewDate'])),df['NewDate'].values,rotation=30 ) 
plt.show()