# !/usr/bin/env python
# coding=utf-8
class FileHandle(object):   # 处理文件的类
    def read(self,path):
        print("Reading File")
        # 读文件                 
    def write(self,path,value):
        __path = path
        print("Writing File")
        # 写文件        
class DBHandle(object):     # 处理数据库的类
    def read(self,path):
        print("Reading DB")
        # 读数据库         
    def write(self,path,value):
        __path = path
        print("Writing DB")
        # 写数据库        
# Tool同时继承了两个类          
class Tool(FileHandle,DBHandle):
#class Tool(DBHandle,FileHandle):
    def businessLogic(self):
        print("In Tool")
tool = Tool()
tool.read("c:\\1.txt")