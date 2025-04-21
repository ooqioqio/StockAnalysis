# !/usr/bin/env python
# coding=utf-8
# 定义并打印字典
onePersonInfo = {'name': 'Mike', 'age': 7}
print(onePersonInfo)        # {'age': 7, 'name': 'Mike'}
onePersonInfo['age'] = 8      # 修改其中的元素
print(onePersonInfo)         # age会变成8
print(onePersonInfo['name']) # Mike
del onePersonInfo['name']
print(onePersonInfo)         # age会变成8 #{'age': 8}
print(onePersonInfo.get('name'))    # None
print(onePersonInfo.get('age'))     # 8
if 'name' not in onePersonInfo:
    onePersonInfo['name'] = "Mike"    # 增加新元素
print(onePersonInfo.get('name'))    # Mike
# 通过for循环遍历字典
print(onePersonInfo)
for i, v in onePersonInfo.items():
    print(i,v) # 得到键和值
