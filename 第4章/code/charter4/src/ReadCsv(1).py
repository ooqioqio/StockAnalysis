# !/usr/bin/env python
# coding=utf-8
import csv,os
fileName="c:\\1\\stock.csv";
if not os.path.isfile(fileName):    # 判断文件是否存在
    print("File not exist!" + fileName)
else: 
    file = open(fileName,'r')       # 以读的模式打开文件
    reader = csv.reader(file)
    for row in reader:              # 逐行读取csv文件
        try:
            print(row)
        except:
            print("Error when Reading Csv file.")
    file.close()                    # 读完后关闭文件      