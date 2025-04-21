# !/usr/bin/env python
# coding=utf-8
import numpy as np 	# 导入numpy库，起了个别名np
arr = np.array(np.arange(4)) # 创建一个序列
print(arr) 			# 输出 [0 1 2 3]
print(np.eye(2)) 	# 创建一个维度是2的对角矩阵，输出如下
# [[1. 0.]
# [0. 1.]]