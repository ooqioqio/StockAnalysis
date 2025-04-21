# !/usr/bin/env python
# coding=utf-8
import numpy as np

arr1 = np.arange(0,1,0.2)
# 输出[0.  0.2 0.4 0.6 0.8]
print(arr1)
# 输出<class 'numpy.ndarray'>
print(type(arr1))
print(arr1.ndim)    # 返回arr1的维数，是1
# 输出[1 2 3 4]
print(np.array(range(1,5)))
arr2=np.array([[1,2,3],[4,5,6]])    # 二维数组
print(arr2.ndim)    # 返回2
print(arr2.size)    # 总长度，返回6
print(arr2.dtype)   # 类型，返回int32
# 形状，返回(2, 3)，表示二维数组，每个维度长度是3
print(arr2.shape) 
arr3=np.array([1,3,5])
print(arr3.mean())  # 计算平均数，返回3
print(arr3.sum())   # 计算和，返回9
# 计算所有行的平均数，返回[2. 5.]
print(arr2.mean(axis=1)) 
# 计算所有列的平均数，返回[2.5 3.5 4.5]
print(arr2.mean(axis=0))