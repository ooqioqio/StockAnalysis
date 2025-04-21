# coding=utf-8
import urllib.request
stockCode = '600895'  # 张江高科
# 请注意，url后没通过问号来传各种参数
url = 'http://quotes.money.163.com/service/chddata.html'
# 参数是通过url.parse的方式来传入的
param = bytes(urllib.parse.urlencode({'code': '0'+stockCode,'start':'20190102','end':'20190102','fields':'TCLOSE;HIGH;LOW;TOPEN;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER'}), encoding='utf8')
# 带各种参数
response = urllib.request.urlopen(url,data=param,timeout=1)
print(response.read().decode("gbk"))
response.close();