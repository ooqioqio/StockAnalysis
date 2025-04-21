# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
# 折线图
x = np.array([1,2,3,4,5])
y = np.array([20,15,18,16,25])
plt.xticks(x, ('20190101','20190105','20190110','20190115','20190120'),color='blue')
plt.yticks(np.arange(10,30,2),rotation=30)
plt.ylim(10,30)
plt.xlabel("Date")
plt.ylabel("Price")
plt.plot(x,y,color="red",linewidth=1)
plt.show()