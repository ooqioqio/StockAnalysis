# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
# 显示中文字符
plt.rcParams['font.sans-serif']=['SimHei'] 
labels = ['工资','股票','基金','著书收益','视频教程收益','其他']
sizes = [23000,2000,2000,1500,2000,800]
explode = (0,0.1,0.1,0.1,0.1,0.1)
colors=['red','blue','green','#ffff00','#ff00ff','#f0f000']
plt.pie(sizes,explode=explode,labels=labels,startangle=45,colors=colors)
plt.title("本月收入情况")
plt.show()