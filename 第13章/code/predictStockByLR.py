# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# 从文件中获取数据
origDf = pd.read_csv('D:/stockData/ch13/6035052018-09-012019-05-31.csv',encoding='gbk')
df = origDf[['Close', 'High', 'Low','Open' ,'Volume']]
featureData = df[['Open', 'High', 'Volume','Low']]
# 划分特征值和目标值
feature = featureData.values
target = np.array(df['Close'])

# 划分训练集，测试集
feature_train, feature_test, target_train ,target_test = train_test_split(feature,target,test_size=0.05)
pridectedDays = int(math.ceil(0.05 * len(origDf)))  # 预测天数
lrTool = LinearRegression()
lrTool.fit(feature_train,target_train)              # 训练
print(lrTool.score(feature_train,target_train))
# 用测试集预测结果
predictByTest = lrTool.predict(feature_test)
# 组装数据
index=0
# 在前95%的交易日中，预测结果和收盘价一致
while index < len(origDf) - pridectedDays:    
    df.ix[index,'predictedVal']=origDf.ix[index,'Close']
    df.ix[index,'Date']=origDf.ix[index,'Date']
    index = index+1
predictedCnt=0
# 在后5%的交易日中，用测试集推算预测股价    
while predictedCnt<pridectedDays:
    df.ix[index,'predictedVal']=predictByTest[predictedCnt]
    df.ix[index,'Date']=origDf.ix[index,'Date']
    predictedCnt=predictedCnt+1
    index=index+1

plt.figure()
df['predictedVal'].plot(color="red",label='predicted Data')
df['Close'].plot(color="blue",label='Real Data')
plt.legend(loc='best')      # 绘制图例
# 设置x坐标的标签
major_index=df.index[df.index%10==0]
major_xtics=df['Date'][df.index%10==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
# 带网格线，且设置了网格样式
plt.grid(linestyle='-.')
plt.show()