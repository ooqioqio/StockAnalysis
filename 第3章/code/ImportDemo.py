# !/usr/bin/env python
# coding=utf-8
import ModuleDemo as tool
from ModuleDemo import Stock as stockTool

print(tool.PI)          # 3.14
print(tool.add(1,2))    # 3
print(tool.minus(1,2))  # -1
tool.displayModuleName() # CalModule
# stockTool.add(1,2)    # 出错
myStockTool = stockTool("600001","10")
myStockTool.buy() #Buy 600001 with the price:10