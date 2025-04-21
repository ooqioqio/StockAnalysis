# !/usr/bin/env python
# coding=utf-8
# 以大括号的方式定义集合
set1 = {'1', '3', '5', '7'}
set2 = {'2', '3', '6', '7'}
# 不能用中括号的方式定义集合，例如 set1 = ['1', '3', '5', '7']
# 交集 
set3 = set1 & set2
print(set3)             # 输出 set(['3', '7'])
print(set1 & set2)      # 输出 set(['3', '7'])   
print(set1.intersection(set2)) # 输出 set(['3', '7'])
# 并集
set4 = set1 | set2
print(set4)             # 输出set(['1', '3', '2', '5', '7', '6'])
print(set1 | set2)      # set(['1', '3', '2', '5', '7', '6'])  
print(set1.union(set2)) # set(['1', '3', '2', '5', '7', '6']) 
# 差集
print(set1 - set2)              # 输出set(['1', '5'])
print(set1.difference(set2))    # 输出set(['1', '5'])
print(set2 - set1)              # 输出set(['2', '6'])
print(set2.difference(set1))    # 输出set(['2', '6'])
# 演示不可变集合的特性
unChangedSet = frozenset(3.14,9.8)
# unChangedSet.add(2.718)
# unChangedSet[0]=2.718
# unChangedSet.discard(3.14)