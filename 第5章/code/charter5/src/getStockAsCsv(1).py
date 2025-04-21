# coding=utf-8
import urllib.request
def getAndSaveStock(stockCodeList,path):
    for stockCode in stockCodeList:
        url = 'http://quotes.money.163.com/service/chddata.html'
        param = bytes(urllib.parse.urlencode({'code': '0'+stockCode,'start':'20190101','end':'20190131','fields':'TCLOSE;HIGH;LOW;TOPEN;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER'}), encoding='utf8')        
        urllib.request.urlretrieve(url, path+stockCode+'.csv',data=param)
# 定义要爬取的股票列表
stockCodeList = []
stockCodeList.append('600895')      # 张江高科
stockCodeList.append('600007')      # 中国国贸        
getAndSaveStock(stockCodeList,'d:\\stockData\\ch5\\')