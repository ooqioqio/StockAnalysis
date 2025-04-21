# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator   = MultipleLocator(5)            # 将x轴主刻度设置为5的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')   # 设置x轴标签的格式
xminorLocator   = MultipleLocator(1)            # 将x轴次刻度设置为1的倍数
ymajorLocator   = MultipleLocator(0.5)          # 将y轴主刻度设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.2f')   # 设置y轴标签的格式
yminorLocator   = MultipleLocator(0.1)          # 将y轴次刻度设置为0.1的倍数
 
x = np.arange(0, 21, 0.1)
ax = plt.subplot(111)
# 设置主刻度标签的位置，标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

# 显示次刻度标签的位置，没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
y = np.sin(x)       # 绘图，图形为y=sinx
plt.plot(x,y)
plt.show()