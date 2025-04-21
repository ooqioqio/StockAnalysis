# !/usr/bin/env python
# coding=utf-8
from pandas import DataFrame
data = {'Date':['20190102','20190103','20190104'],'Open':[10,10.5,10.2],'Close':[10.5,10.2,10.3]}
df1 = DataFrame(data)
'''
   Close      Date  Open
0   10.5  20190102  10.0
1   10.2  20190103  10.5
2   10.3  20190104  10.2
'''
print(df1)
df2 = DataFrame(data, columns=['Date','Open','Close'])
'''
       Date  Open  Close
0  20190102  10.0   10.5
1  20190103  10.5   10.2
2  20190104  10.2   10.3
'''
print(df2)
df2 = DataFrame(data, columns=['Date','Open','Close'])
print(df2)
df3 = DataFrame(data, columns=['Date','Open','Close'], index=['1','2','3'])
'''
       Date  Open  Close
1  20190102  10.0   10.5
2  20190103  10.5   10.2
3  20190104  10.2   10.3
'''
print(df3)       