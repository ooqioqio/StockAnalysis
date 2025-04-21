# !/usr/bin/env python
# coding=utf-8
# 定义两个元组
cityTup = ("TianJin","WuHan","ChengDu")
#cityTup[0] = "HeFei" # 会抛出异常
#del cityTup[0] # 无法删除其中的元素，则会抛出异常
print(cityTup)  # 输出结果是('TianJin', 'WuHan', 'ChengDu')
# 把列表转为元组
bookList = ["Python book","Java Book"]
bookTup = tuple(bookList) #把列表转为元组
print(bookTup)  # 输出结果是('Python book', 'Java Book')
# 查询操作
print(cityTup[1])   # 输出WuHan
print(cityTup[0:2]) # 输出('TianJin', 'WuHan')

#统计元组里指定元素的个数
print(cityTup.count("TianJin"))  # 返回1
#统计元组的长度
print(len(cityTup))  # 返回3

# 只能删除整个元组对象
del cityTup
