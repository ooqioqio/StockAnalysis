# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5) 
plt.figure()        # 设置白板
plt.subplot(2,1,1)  # 第一个子图在2*1的第1个位置
plt.plot(x,x*x)
plt.subplot(2,2,3)  # 第二个子图在2*2的第3个位置
plt.plot(x,1/x)
plt.subplot(224)    # 第三个子图在2*2的第4个位置
plt.plot(x,x*x*x)
plt.show()