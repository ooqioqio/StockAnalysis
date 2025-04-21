# !/usr/bin/env python
# coding=utf-8
from matplotlib.dates import WeekdayLocator, DayLocator, MONDAY
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import datetime as dt
 
fig = plt.figure()
ax = fig.add_subplot(111)   # 定义图的位置
startDate = dt.datetime(2019,4,1)
endDate = dt.datetime(2019,4,30)
interval = dt.timedelta(days=1)
dates = mpl.dates.drange(startDate, endDate, interval)
y = np.random.rand(len(dates))*10               # 产生若干个随机数
ax.plot_date(dates, y, linestyle='-.')          # 设置时间序列
# ax.plot_date(dates, y, linestyle='-.')        # 可以查看这个样式
dateFmt = mpl.dates.DateFormatter('%Y-%m-%d')   # 时间的显示格式
# 设置主刻度和次刻度的时间
mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
ax.xaxis.set_major_formatter(dateFmt)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
fig.autofmt_xdate()     # 自动旋转
plt.show()