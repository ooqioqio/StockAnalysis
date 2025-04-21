# !/usr/bin/env python
# coding=utf-8
# 定义类
class Car:       
    def __init__(self,area):              
        self.__area = area  
    def get_area(self):
        return self.__area
    def set_area(self,area):
        self.__area = area   
# 使用类        
carForPeter = Car("ShangHai")
carForPeter.__area="HangZhou"
print(carForPeter.get_area())       # 发现并没改变__area
carForPeter.set_area("WuXi")
print(carForPeter.get_area())       # WuXi
carForPeter._Car__area="Bad Usage"  # 不建议这样做
print(carForPeter.get_area())       # 发现改了__area的值