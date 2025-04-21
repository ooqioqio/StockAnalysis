# !/usr/bin/env python
# coding=utf-8
class Employee(object):   
    def __init__(self,name):
        self.__name = name          
    def work(self):
        print(self.__name + " Work.")      
class Manager(Employee):    
    def __init__(self,name):
        self.__name = name
    def check(self):
        print("Manage check work.")    
    def work(self):
        print(self.__name + " Work.")
        self.check()
class HR(Employee):    
    def __init__(self,name):
        self.__name = name
    def calSalary(self):
        print("HR calculate Salary.")    
    def work(self):
        print(self.__name + " Work.")
        self.calSalary()        
# 调用类
manager = Manager("Peter")
manager.work()
hr = HR("Mike")
hr.work()
