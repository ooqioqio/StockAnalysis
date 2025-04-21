# !/usr/bin/env python
# coding=utf-8
# 定义类
class Car:       
    def __init__(self,owner,area):
        self.owner = owner      
        self.__area = area  
    def __engineStart(self):
        print("Engine Start")
    def start(self):
        print("Start Car")
        self.__engineStart()         
    def get_area(self):
        return self.__area
    def set_area(self,area):
        self.__area = area   
# 使用变量   
carForPeter = Car("Peter",'ShangHai')
# print(carForPeter.__area)
print(carForPeter.owner) # Peter
carForPeter.set_area("HangZhou")
print(carForPeter.get_area())   # HangZhou
carForPeter.start()        
# carForPeter.__engineStart()    # 会报错