# !/usr/bin/env python
# coding=utf-8
stockInfoList = ['600001','600002']
try:
    #stockInfoList.remove('600003')
    stockInfoList.remove('600001')
except: 
    print('Could not Remove from List')
finally:
    print('in finally')    
print('following job')      