# !/usr/bin/env python
# coding=utf-8
from functools import cmp_to_key

# 定义降序规则
def desc(x, y):
    if x < y:
        return 1    # 如果x小于y，则x排在y之前
    elif x > y:
        return -1   # 如果大于y，则x排在y之后
    else:
        return 0    # 否则并列

# 定义待排序的numbers列表  
numbers = [5, 58, 47 ,75 ,100]
# 使用 cmp_to_key 转换旧的比较函数
# numbers.sort(key=cmp_to_key(desc)) 
# # 在Python 3中，print是函数，需要使用括号
# print(numbers)      # 输出[100, 75, 58, 47, 5]
# numbers.sort()
# print(numbers)      # 输出[5, 47, 58, 75, 100]
ascending_numbers = sorted(numbers)  # 用更简单的方法升序排序
descending_numbers = sorted(numbers, reverse=True)  # 以及降序排序
print(ascending_numbers)  # 输出[5, 47, 58, 75, 100]
print(descending_numbers)  # 输出[100, 75, 58, 47, 5]
