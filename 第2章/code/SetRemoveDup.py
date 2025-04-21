# !/usr/bin/env python
# coding=utf-8
# 调用集合的方法把列表转换成集合
set1 = set(["a", "a", "b", "b", "c"])
print(set1) # 输出set(['a', 'c', 'b'])
# 添加元素
set1.add("d")
set1.add("c")   # 由于重复，因此无法添加
print(set1)     # set(['a', 'c', 'b', 'd'])

set2 = set1.copy()
set1.clear()
print(set1)     # 由于已清空，因此输出set([])
print(set2)     # set(['a', 'c', 'b', 'd'])

set2.discard("f") # 删除元素，哪怕没找到也不会抛出异常

list=[1,1,2,2,3,3,4,4,5] # 含重复元素的列表
setFromList=set(list)    # 通过集合去掉重复的元素
print(setFromList)       # 输出为set([1, 2, 3, 4, 5])