# !/usr/bin/env python
# coding=utf-8

priceList = [10.58,25.47,100.58] # 浮点型列表
cityList = ["ShangHai", "HangZhou", "NanJing"] # 字符串类型列表
mixList = [1, 3.14, "Company"] #混合类型的列表，谨慎使用
  
# 在控制台输出
print(priceList)  #[10.58, 25.47, 100.58]
print(cityList)   #['ShangHai', 'HangZhou', 'NanJing']
print(mixList)    #[1, 3.14, 'Company']

del mixList[2]
print(mixList)    # 没有了最后一个元素
#mixArr.remove(2) # 去掉没有的元素，也会抛出异常
mixList.remove(1)
print(mixList)    # 也看不到1了

print(priceList[0])      # 获得数组指定位置的元素，这里输出的是10.58
priceList.append(200.74) # 添加元素
print(priceList)         # 能看到添加后的元素
print(cityList.index("ShangHai"));
#print(cityList.index("DaLian")); # 如果找不到元素，会抛出异常并终止程序
#下面是额外添加的对关于对集合的添加操作
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # 输出: {1, 2, 3, 4}
#下面是额外添加的对于字典的添加操作
student = {"name": "张三", "age": 20}
new_info = {"gender": "男", "city": "北京"}
student.update(new_info)
print(student)  # 输出: {'name': '张三', 'age': 20, 'gender': '男', 'city': '北京'}


