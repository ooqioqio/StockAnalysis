# !/usr/bin/env python
# coding=utf-8
stockPirceList = [100,200,'600001',300,400]
# try:
#   for item in stockPirceList:
#      print("Current Price：",item + 100)
# except: 
#    print('Error when printing current price.')
for item in stockPirceList:
    try:
      print("Current Price：",item + 100)
    except: 
        print('Error when printing current price.')