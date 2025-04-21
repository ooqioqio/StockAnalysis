# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl
# 计算BIAS的方法，入参periodList传入周期列表 
def calBIAS(df,periodList):
    # 遍历周期，计算6,12,24日BIAS
    for period in periodList:
        df['MA'+str(period)] = df['Close'].rolling(window=period).mean() 
        df['MA'+str(period)].fillna(value = df['Close'], inplace = True)
        df['BIAS'+str(period)] = (df['Close'] - df['MA'+str(period)])/df['MA'+str(period)]*100 
    return df
filename='D:\\stockData\ch11\\6006402019-01-012019-05-31.csv'
df = pd.read_csv(filename,encoding='gbk')
list = [6,12,24]    # 周期列表
# 调用方法计算BIAS
stockDataFrame = calBIAS(df,list) 
# print(stockDataFrame) # 可以去掉注释来查看结果
figure = plt.figure()
# 创建子图     
(axPrice, axBIAS) = figure.subplots(2, sharex=True)
# 调用方法，在axPrice子图中绘制K线图
candlestick2_ochl(ax = axPrice, 
              opens=df["Open"].values, closes=df["Close"].values,
              highs=df["High"].values, lows=df["Low"].values,
              width=0.75, colorup='red', colordown='green')
axPrice.set_title("K线图和均线图")    # 设置子图标题
stockDataFrame['Close'].rolling(window=6).mean().plot(ax=axPrice,color="red",label='6日均线')
stockDataFrame['Close'].rolling(window=12).mean().plot(ax=axPrice,color="blue",label='12日均线')
stockDataFrame['Close'].rolling(window=24).mean().plot(ax=axPrice,color="green",label='24日均线')
axPrice.legend(loc='best')      # 绘制图例
axPrice.set_ylabel("价格（单位：元）")
axPrice.grid(linestyle='-.')    # 带网格线        
# 在axBIAS子图中绘制BIAS图形
stockDataFrame['BIAS6'].plot(ax=axBIAS,color="blue",label='BIAS6')
stockDataFrame['BIAS12'].plot(ax=axBIAS,color="green",label='BIAS12')
stockDataFrame['BIAS24'].plot(ax=axBIAS,color="purple",label='BIAS24')
plt.legend(loc='best')          # 绘制图例
plt.rcParams['font.sans-serif']=['SimHei']       
axBIAS.set_title("BIAS指标图")  # 设置子图的标题
axBIAS.grid(linestyle='-.')     # 带网格线
# 设置x轴坐标的标签和旋转角度
major_index=stockDataFrame.index[stockDataFrame.index%5==0]
major_xtics=stockDataFrame['Date'][stockDataFrame.index%5==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.show()