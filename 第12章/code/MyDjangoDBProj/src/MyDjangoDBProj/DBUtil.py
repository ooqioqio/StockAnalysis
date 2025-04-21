# !/usr/bin/env python
# coding=utf-8
from django.http import HttpResponse
from . import models
 
def insertStock(request):
    stockInfo = models.stockInfo(date='20190101',open=10.0,close=10.5,high=10.7,low=10.3,vol=10,stockCode='DemoCode')
    stockInfo.save()    
    return HttpResponse("OK!")

def insertMoreStock(request):
    stockInfoList=[]
    stock1 = models.stockInfo(date='20190101',open=10.0,close=10.5,high=10.7,low=10.3,vol=10,stockCode='DemoCode')
    stockInfoList.append(stock1)
    stock2 = models.stockInfo(date='20190102',open=10.5,close=11,high=11.2,low=10.8,vol=12,stockCode='DemoCode')
    stockInfoList.append(stock2)
    models.stockInfo.objects.bulk_create(stockInfoList)
    return HttpResponse("OK!")

def deleteStock(request):
    # 删除所有数据记录
    # models.stockInfo.objects.all().delete()
    # 删除指定数据记录
    models.stockInfo.objects.filter(date='20190101',stockCode='DemoCode').delete()
    return HttpResponse("OK!")

def updateStock(request):
    # 找到数据记录并更新
    models.stockInfo.objects.filter(date='20190101',stockCode='DemoCode').update(open=12,close=13)
    return HttpResponse("OK!")

def getAllStock(request):
    stockInfoList = models.stockInfo.objects.all()
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def getStockWithFilter(request):
    stockInfoList = models.stockInfo.objects.filter(date='20190101')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoLike(request):
    # 返回包含2019的股票数据
    stockInfoList = models.stockInfo.objects.filter(date__contains='2019')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoStartswith(request):
    # 返回以2019开头的股票数据
    stockInfoList = models.stockInfo.objects.filter(date__startswith='2019')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoEndswith(request):
    # 返回以2019结束的股票数据
    stockInfoList = models.stockInfo.objects.filter(date__endswith='2019')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoRange(request):
    # 大于8，小于12
    # stockInfoList = models.stockInfo.objects.filter(open__gt=8,open__lt=12)
    # 大于等于8，小于等于12
    stockInfoList = models.stockInfo.objects.filter(open__gte=8,open__lte=12)
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

from django.db import connection
def demoSQL(request):
    cursor = connection.cursor()
    try:
        cursor.execute('select * from stockInfo')
        result=cursor.fetchall()
    finally:
        cursor.close()    
    return HttpResponse(result)