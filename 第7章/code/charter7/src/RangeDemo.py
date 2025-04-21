# !/usr/bin/env python
# coding=utf-8
# 输出0到4的整数，但不包含5
for val in range(0,5): 
# 等价for val in range(0,5,1):    
    print(val)
# 输出0,2,4
for val in range(0,5,2):
    print(val)
# 如下代码会出错，因为range不支持浮动类型
for val in range(0,5,0.5):
    print(val)