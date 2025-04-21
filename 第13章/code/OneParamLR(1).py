# !/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
 
# 从文件中读数据，并转换成DataFrame格式
dataset=datasets.load_boston()
data=pd.DataFrame(dataset.data)
data.columns=dataset.feature_names  # 特征值
data['HousePrice']=dataset.target   # 房价，即目标值
 
# 这里单纯计算离中心区域的距离和房价的关系
dis=data.loc[0:data['DIS'].size-1,'DIS'].as_matrix()
housePrice=data.loc[0:data['HousePrice'].size-1,'HousePrice'].as_matrix()
 
# 转置一下，否则数据是竖排的
dis=np.array([dis]).T
housePrice=np.array([housePrice]).T
 
# 训练线性模型
lrTool=LinearRegression()
lrTool.fit(dis,housePrice)
# 输出系数和截距 
print(lrTool.coef_)
print(lrTool.intercept_)  
 
# 画图显示
plt.scatter(dis,housePrice,label='Real Data')
plt.plot(dis,lrTool.predict(dis),c='R',linewidth='2',label='Predict')

print(lrTool.score(dis,housePrice))
print(r2_score(housePrice, lrTool.predict(dis)))

# 验证数据
print(dis[0])
print(lrTool.predict(dis)[0])
print(dis[2])
print(lrTool.predict(dis)[2])

plt.legend(loc='best')      # 绘制图例
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("DIS与房价的线性关系")
plt.xlabel("DIS")
plt.ylabel("HousePrice")
plt.show()