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
# 改写后的Tool类          
class Tool(object):    
    def __init__(self,fileHandle):
        self.fileHandle = fileHandle
        self.dbHandle = DBHandle()
    def calDataInFile(self,path):
        self.fileHandle.read(path)        
        # 统计文件中的数据
    def calDataInDB(self,path):
        self.dbHandle.read(path)        
        # 统计文件中的数据
# 使用类        
fileHandle =  FileHandle()       
tool = Tool(fileHandle)
tool.calDataInFile("c:\\1.txt")         # 输出Reading File
tool.calDataInDB("localhost:3309/myDB") # 输出Reading DB