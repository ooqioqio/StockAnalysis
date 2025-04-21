# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
import pymysql
import sys
from mpl_finance import candlestick2_ochl
from matplotlib.ticker import MultipleLocator
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
    return df
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
# print(calMACD(df, 12, 26, 9))     # 输出结果      
stockDataFrame = calMACD(df, 12, 26, 9)
# 开始绘图，设置大小，共享x坐标轴
figure,(axPrice, axMACD) = plt.subplots(2, sharex=True, figsize=(15,8))
# 调用方法绘制K线图 
candlestick2_ochl(ax = axPrice, 
                  opens=stockDataFrame["open"].values, closes=stockDataFrame["close"].values,
                  highs=stockDataFrame["high"].values, lows=stockDataFrame["low"].values,
                  width=0.75, colorup='red', colordown='green')
axPrice.set_title("600895张江高科K线图和均线图")     # 设置子图标题
stockDataFrame['close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均线')
stockDataFrame['close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均线')
stockDataFrame['close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均线')
axPrice.legend(loc='best')      # 绘制图例
axPrice.set_ylabel("价格（单位：元）")
axPrice.grid(linestyle='-.')    # 带网格线
# 开始绘制第二个子图
stockDataFrame['DEA'].plot(ax=axMACD,color="red",label='DEA')
stockDataFrame['DIF'].plot(ax=axMACD,color="blue",label='DIF')
plt.legend(loc='best')          # 绘制图例
# 设置第二个子图中的MACD柱状图
for index, row in stockDataFrame.iterrows():
    if(row['MACD'] >0):         # 大于0则用红色
        axMACD.bar(row['date'], row['MACD'],width=0.5, color='red')        
    else:                       # 小于等于0则用绿色 
        axMACD.bar(row['date'], row['MACD'],width=0.5, color='green')
axMACD.set_title("600895张江高科MACD")  # 设置子图的标题
axMACD.grid(linestyle='-.')     # 带网格线
# xmajorLocator = MultipleLocator(10)     # 将x轴的主刻度设置为10的倍数
# axMACD.xaxis.set_major_locator(xmajorLocator)
major_xtics=stockDataFrame['date'][stockDataFrame.index%10==0]
axMACD.set_xticks(major_xtics)
# 旋转x轴显示文字的角度
for xtick in axMACD.get_xticklabels():
    xtick.set_rotation(30)    
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
plt.show()