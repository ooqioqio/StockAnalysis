# !/usr/bin/env python
# coding=utf-8
import myPackage.CalModuleDemo as calTool
from myPackage import ModuleDemo as myTool  
print(myTool.PI)                # 3.14
print (calTool.calGravity(10))  # 98.0
print (calTool.E)               # 2.718