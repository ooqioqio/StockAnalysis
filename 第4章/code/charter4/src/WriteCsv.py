# !/usr/bin/env python
# coding=utf-8
import csv  # 导入csv模块
head=['code','price','Date']
stock1=['600001',26,'20181212']
stock2=['600002',32,'20181212']
stock3=['600003',32,'20181212']
# 以'a'追加写模式打开文件
file = open('c:\\1\\stock.csv','a',newline='')
# 设置写入的对象
write = csv.writer(file)
# 写入具体的内容
write.writerow(head)
write.writerow(stock1)
write.writerow(stock2)
write.writerow(stock3)
print("Finishe Writing CSV File.")