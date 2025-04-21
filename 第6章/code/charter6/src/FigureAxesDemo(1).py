# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 20)
# 划分子图
fig,axes=plt.subplots(2,2)
ax1=axes[0,0]
ax2=axes[0,1]
ax3=axes[1,0]
ax4=axes[1,1]

ax1.plot(x, x)
ax1.grid(color='blue', linestyle='--')
ax2.grid(color='red', linewidth=2)
ax2.plot(x, -x)
ax3.grid(axis="y")
ax3.plot(x, np.cos(x))
ax4.grid(axis="x")
ax4.plot(x, np.sin(x))
plt.show()