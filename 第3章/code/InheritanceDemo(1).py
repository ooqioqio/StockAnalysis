# !/usr/bin/env python
# coding=utf-8
class Employee(object):   # 定义一个父类
    def __init__(self,name):
        self.__name = name  
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name        
    def login(self):    # 父类中的方法
        print("Employee In Office")
    def changeSalary(self,newSalary):
        self._salary = newSalary
    def get_Salary(self):
        return self._salary    
# 定义一个子类，继承Employee类          
class Manager(Employee):    
    def login(self):    # 在子类中覆盖父类的方法
        print("Manager In Office")
        print("Check the Account List")
    def attendWeeklyMeeting(self):
        print("Manager attend Weekly Meeting")
# 使用类 
manager = Manager("Peter")
print(manager.get_name())   # Peter
manager.login()             # 调用子类的方法，Manager In Office
manager.changeSalary(30000)
print(manager.get_Salary()) # 30000
manager.attendWeeklyMeeting()
