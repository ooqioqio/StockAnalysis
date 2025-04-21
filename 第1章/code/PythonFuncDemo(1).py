# !/usr/bin/env python
# coding=utf-8
# 定义没返回的函数
def printMsg(x,y):
    print (f"x is {x}")
    print (f"y is {y}")
# 通过return返回
def add(x,y):
    return x + y
1
# 调用函数
printMsg(1,2)
printMsg("1",2) 	# 会报错，这就是不注意参数类型的后果
print (add(100,50))

