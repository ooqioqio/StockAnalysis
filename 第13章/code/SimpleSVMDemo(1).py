# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
# 给出平面上的若干点
points = np.r_[[[-1,1],[1.5,1.5],[1.8,0.2],[0.8,0.7],[2.2,2.8],[2.5,3.5],[4,2]]]
# 按0和1标记成两类
typeName = [0,0,0,0,1,1,1]

# 建立模型
svmTool = svm.SVC(kernel='linear')
svmTool.fit(points,typeName)    # 传入参数

# 确立分类的直线
sample = svmTool.coef_[0]       # 系数
slope = -sample[0]/sample[1]    # 斜率
lineX = np.arange(-2,5,1)       # 获取-2到5，间距是1的若干数据
lineY = slope*lineX-(svmTool.intercept_[0])/sample[1]
# 画出划分直线
plt.plot(lineX,lineY,color='blue',label='Classified Line')
plt.legend(loc='best')          # 绘制图例
plt.scatter(points[:,0],points[:,1],c='R')
plt.show()