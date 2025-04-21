# !/usr/bin/env python
# coding=utf-8
class Shape:    # 定义父类
    _size=0     # 受保护的属性
    def __init__(self,type,size):              
        self._type = type  
        self._size = size
    def _set_type(self,type):   # 受保护的方法
        self._type=type
    def _get_type(self):        # 受保护的方法
        return self._type
class Circle(Shape):        # 定义子类
    def set_size(self,size): 
       self._size = size    # 覆盖了父类的_size属性
    def printSize(self): 
       print(self._size)    
class anotherClass:         # 定义不相干的一个类
    pass                    # 如果是空方法，则需要加个pass，否则会报错
# 使用子类
c=Circle("Square",2)
c._set_type("Circle")
print(c._get_type())
c.printSize()
anotherClass._set_type("Circle")  # 会报错