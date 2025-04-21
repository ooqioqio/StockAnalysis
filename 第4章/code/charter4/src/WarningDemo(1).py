# !/usr/bin/env python
# coding=utf-8
import warnings
warnings.filterwarnings("ignore")
stockInfoList = ['600001','600002']
try:
    stockInfoList.remove('600003')
except: 
    warnings.warn('Could not Remove from List')
finally:
    print('in finally')    
print('following job')      