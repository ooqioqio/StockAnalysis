# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
import pymysql
import sys
# 第一个参数是数据，第二个参数是周期
def calEMA(df, term): 
    for i in range(len(df)):
        if i==0:    # 第一天
            df.ix[i,'EMA']=df.ix[i,'close']
        if i>0:
            df.ix[i,'EMA']=(term-1)/(term+1)*df.ix[i-1,'EMA']+2/(term+1)*df.ix[i,'close']
    EMAList=list(df['EMA'])
    return EMAList
# 定义计算MACD的方法 
def calMACD(df, shortTerm=12, longTerm=26, DIFTerm=9):
    shortEMA = calEMA(df, shortTerm)
    longEMA = calEMA(df, longTerm)
    df['DIF'] = pd.Series(shortEMA) - pd.Series(longEMA)
    for i in range(len(df)):
        if i==0:    # 第一天
            df.ix[i,'DEA'] = df.ix[i,'DIF']     # ix可以通过标签名和索引来获取数据
        if i>0:  
            df.ix[i,'DEA'] = (DIFTerm-1)/(DIFTerm+1)*df.ix[i-1,'DEA'] + 2/(DIFTerm+1)*df.ix[i,'DIF']  
    df['MACD'] = 2*(df['DIF'] - df['DEA'])
    return df[['date','DIF','DEA','MACD']]
    # return df
try:
    # 打开数据库连接
    db = pymysql.connect("localhost","root","123456","pythonStock" )
except:
    print('Error when Connecting to DB.')   
    sys.exit()  
cursor = db.cursor()
cursor.execute("select * from stock_600895")
cols = cursor.description   # 返回列名
heads = []
# 依次把每个cols元素中的第一个值放入col数组
for index in cols:
    heads.append(index[0])
result = cursor.fetchall()
df = pd.DataFrame(list(result))
df.columns=heads
print(calMACD(df, 12, 26, 9))   # 输出结果      
stockDataFrame = calMACD(df, 12, 26, 9)
# 开始绘图
plt.figure()
stockDataFrame['DEA'].plot(color="red",label='DEA')
stockDataFrame['DIF'].plot(color="blue",label='DIF')
plt.legend(loc='best')      # 绘制图例
# 设置MACD柱状图
for index, row in stockDataFrame.iterrows():
    if(row['MACD'] >0):     # 大于0则用红色
        plt.bar(row['date'], row['MACD'],width=0.5, color='red')        
    else:                   # 小于等于0则用绿色 
        plt.bar(row['date'], row['MACD'],width=0.5, color='green')
# 设置x轴坐标的标签和旋转角度
major_index=stockDataFrame.index[stockDataFrame.index%10==0]
major_xtics=stockDataFrame['date'][stockDataFrame.index%10==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
# 带网格线，且设置了网格样式
plt.grid(linestyle='-.') 
plt.title("600895张江高科的MACD图")
plt.rcParams['axes.unicode_minus'] = False 
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()