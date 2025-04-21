# !/usr/bin/env python
# coding=utf-8
class CalculateTool:
    __PI = 3.14
    @staticmethod
    def add(x,y):
        __result = x+y
        print(x + y) 
    @classmethod
    def calCircle(self,r):
        print(self.__PI*r*r)
CalculateTool.add(23, 22) 		# 输出45
CalculateTool.calCircle(1) 	    # 输出3.14  
# 不建议通过对象访问静态方法和类方法
tool = CalculateTool()
tool.add(23, 22)
tool.calCircle(1)