# coding=utf-8
# Print Hello World
from pandas import Series
import pandas as pd
s1 = Series(range(5),index = ["one","two","three","four","five"])
'''
s1.head(2) 输出如下
one    0
two    1
dtype: int32
'''
print(s1.head(2))   # 如果不带参数，默认返回前5个
'''
s1.tail(2) 输出如下
four    3
five    4
dtype: int32
'''
print(s1.tail(2))   # 如果不带参数，默认返回后5个
'''
s1.take([1,3]) 输出如下
two     1
four    3
dtype: int32
'''
print(s1.take([1,3])) # 返回指定位置的元素
'''
以切片的方式访问，如下两句的输出是一样的
two      1
three    2
dtype: int32
'''
print(s1[1:3]) 
print(s1['two':'three'])