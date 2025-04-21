# !/usr/bin/env python
# coding=utf-8
import numpy as np
arr1 = np.arange(0,11,1)
# 输出[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr1)
arrSplit1 = arr1[2:5]
# 输出[2 3 4]
print(arrSplit1)
# 输出[2 3 4 5 6 7 8 9]，不包含10
print(arr1[2:-1])		# -1表示最右边的元素
# 输出[ 2  3  4  5  6  7  8  9 10]
print(arr1[2:])		# 表示从2号索引开始到最后，包含10
# 输出[0 1 2 3 4]
print(arr1[:5])		# 表示从0号索引开始到5号索引
# 输出[2 3 4 5 6 7 8]
print(arr1[2:-2])		# -2表示右边开始第2个元素
# 输出[0 1 2 3 4 5 6 7]
print(arr1[:-3])		# -3表示右边开始第3个元素
# 针对多维数组的切片
arr2 = np.array([[1, 2, 3],[4, 5, 6]])
# a输出[[2 3]
#       [5 6]]
print(arr2[[0,1],1:])