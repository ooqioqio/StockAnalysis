# !/usr/bin/env python
# coding=utf-8
# 第3个参数是lambda表达式
def add(x,y,func):
    return func(x) + func(y)
print(add(2,4,lambda a:a*a)) # 2的平方加4的平方等于20

print("My Stock List".find("stock")) # 输出-1，表示没找到
def existKey(key,words,func):
    return func(words).find(key)
# 输出3，表示找到了
print(existKey("stock","My Stock List" ,lambda words:words.lower()))