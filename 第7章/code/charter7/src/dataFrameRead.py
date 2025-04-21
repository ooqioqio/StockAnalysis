# !/usr/bin/env python
# coding=utf-8
from pandas import DataFrame
data = {'Date':['20190102','20190103','20190104'],'Open':[10,10.5,10.2],'Close':[10.5,10.2,10.3]}
df = DataFrame(data, columns=['Date','Open','Close'], index=['1','2','3'])
# 输出Index(['1', '2', '3'], dtype='object')
print(df.index)     # 查看索引
# 输出Index(['Date', 'Open', 'Close'], dtype='object')
print(df.columns)   # 查看列名
'''
[['20190102' 10.0 10.5]
 ['20190103' 10.5 10.2]
 ['20190104' 10.2 10.3]]
'''
print(df.values)    # 查看数值
# 输出[10.  10.5 10.2]
print(df['Open'].values)    # 查看指定列的数值
'''
Date     20190102
Open           10
Close        10.5
Name: 1, dtype: object
'''
print(df.loc['1'])          # 查看指定索引行的数值
# 查看指定行的数值，结果等同print(df.loc['1']) 
print(df.iloc[0])