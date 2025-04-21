# !/usr/bin/env python
# coding=utf-8
import numpy as np
print(np.abs(-10))      # 求绝对值，该表达式返回10
print(np.around(1.2))   # 去掉小数位数，该表达式返回1
print(np.round_(1.7))   # 四舍五入，该表达式返回2
print(np.ceil(1.1))     # 求大于或等于该数的整数，该表达式返回2
print(np.floor(1.1))    # 求小于或等于该数的整数，该表达式返回1
print(np.sqrt(16))      # 求平方根值，该表达式返回4
print(np.square(6))     # 求平方，该表达式返回36
print(np.sign(6))       # 符号函数，如果大于0则返回1，该表达式返回1
print(np.sign(-6))      # 符号函数，如果小0则返回-1，该表达式返回-1
print(np.sign(0))       # 符号函数，如果等于0则返回0，该表达式返回0
print(np.log10(100))    # 求以10为底的对数，该表达式返回2
print(np.log2(4))       # 求以2为底的对数，该表达式返回2
print(np.exp(1))        # 求以e为底的幂次方，该表达式返回e
print(np.power(2,3))    # 求2的3次方，该表达式返回8