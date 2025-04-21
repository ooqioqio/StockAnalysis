# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-2,3)
plt.xlim(-2,2)
plt.plot(x,2*x,color="red",label='y=2x')
plt.plot(x,3*x,color="blue",label='y=3x')
plt.legend(loc='2')
# plt.legend(loc='upper left' ) 和第9行等价
plt.title("Func Demo",fontsize='large',fontweight='bold',loc ='center')
plt.show()