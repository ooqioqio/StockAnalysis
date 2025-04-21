# !/usr/bin/env python
# coding=utf-8
from sklearn import preprocessing
import numpy as np

origVal = np.array([[10,5,3],
                   [8,6,12],
                   [14,7,15]])
# 计算均值
avgOrig = origVal.mean(axis=0)
# 计算标准差
stdOrig=origVal.std(axis=0)

print((origVal-avgOrig)/stdOrig)
scaledVal=preprocessing.scale(origVal)

print(scaledVal)