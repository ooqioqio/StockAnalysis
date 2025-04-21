# !/usr/bin/env python
# coding=utf-8

print("Hello 'World'")       # 双引号单引号夹杂使用
print('Hello "World"')       # 单引号里套双引号
print("Hello: \nMy name is Peter.") # \n是换行符
print(r"Hello \name is Peter.") # 加了前缀r，则会原样输出
str_var = "123456789"  # 避免使用内置函数名作为变量名
print(str_var.index("234"))   	# 查找234这个字符串的位置，返回1 
#print(str_var.index("256"))  	# 没找到则会抛出异常
print(str_var.find("456"))    	# 查找456所在的位置，返回3
print(str_var.find("256"))    	# 没找到，返回-1 inde
print(len(str_var))            	# 返回长度，结果是9
print(str_var.replace("234", "334"))  # 把234替换成334

