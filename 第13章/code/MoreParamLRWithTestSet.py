# !/usr/bin/env python
# coding=utf-8
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

 
dataset = datasets.load_boston()
# 特征值集合，不包括目标值房价
featureData = dataset.data
housePrice = dataset.target
# 划分训练集和测试集，测试集的比例是10% 
featureTrain, featureTrainTest, housePriceTrain, housePriceTest = train_test_split(featureData, housePrice, test_size=0.1)
# 构建线性回归对象 
lrTool = LinearRegression()
# 用训练集来拟合参数
lrTool.fit(featureTrain, housePriceTrain)
# 用训练集绘图
plt.scatter(housePriceTrain,lrTool.predict(featureTrain),c='R',label='Predicted Data')
plt.scatter(housePriceTrain,housePriceTrain,label='Real Data')
# 用测试集来计算方差
predictByTest = lrTool.predict(featureTrainTest)
# 用测试集计算方差
testResult = np.sum(((predictByTest - housePriceTest) ** 2) / len(housePriceTest))
print(testResult)
plt.show()