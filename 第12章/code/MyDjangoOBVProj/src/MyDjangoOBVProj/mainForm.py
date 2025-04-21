# !/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
import pandas_datareader
import matplotlib.pyplot as plt
import pandas as pd
from mpl_finance import candlestick2_ochl
import sys
from io import BytesIO
import base64
import imp
from . import models
imp.reload(sys)
import logging
from django.db import connection
# 引用django日志实例
logger = logging.getLogger(__name__)
# logger = logging.getLogger('loggers')
def display(request):
    logger.info("start to display main.html")
    return render(request, 'main.html')

# 计算OBV的方法 
def calOBV(df):
    logger.info("start calOBV")
    # 把成交量换算成万手
    df['VolByHand'] = df['Volume']/1000000
    # 创建OBV列，先全填充为0
    df['OBV'] =0  
    cnt=1   # 索引从1开始，即从第2天算起
    while cnt<=len(df)-1:
        if(df.iloc[cnt]['Close']>df.iloc[cnt-1]['Close']):
            df.ix[cnt,'OBV'] = df.ix[cnt-1,'OBV'] + df.ix[cnt,'VolByHand']
        if(df.iloc[cnt]['Close']<df.iloc[cnt-1]['Close']):            
            df.ix[cnt,'OBV'] = df.ix[cnt-1,'OBV'] - df.ix[cnt,'VolByHand']   
        cnt=cnt+1   
    return df

def insertData(stockCode,startDate,endDate):
    logger.info("start insertData")
    # 先删除
    models.stockInfo.objects.filter(stockCode=stockCode).delete()
    stock = pandas_datareader.get_data_yahoo(stockCode+'.ss',startDate,endDate)
    # 删除最后一天多余的股票交易数据
    stock.drop(stock.index[len(stock)-1],inplace=True)
    filename='D:\\stockData\ch12\\'+stockCode+startDate+endDate+'.csv'
    stock.to_csv(filename)
    stock = pd.read_csv(filename,encoding='gbk')
    cnt=0
    # 存入数据库
    stockInfoList=[]
    while cnt<=len(stock)-1:
        date=stock.iloc[cnt]['Date']
        open=float(stock.iloc[cnt]['Open'])
        close=float(stock.iloc[cnt]['Close'])
        high=float(stock.iloc[cnt]['High'])
        low=float(stock.iloc[cnt]['Low'])
        vol=int(stock.iloc[cnt]['Volume'])        
        stockOne = models.stockInfo(date=date,open=open,close=close,high=high,low=low,vol=vol,stockCode=stockCode)
        stockInfoList.append(stockOne)
        cnt=cnt+1
    models.stockInfo.objects.bulk_create(stockInfoList)
    return stock

def loadStock(stockCode,startDate,endDate):
    logger.info("start loadStock")
    # 先从数据表中获取数据
    cursor = connection.cursor()
    try:
        cursor.execute("select date,high,low,open,close,vol from stockInfo where stockCode='"+stockCode+"' and date>='"+startDate+"' and date<='"+endDate+"'")
        heads = ['Date','High','Low','Open','Close','Volume']
        # 依次把每个cols元素中的第一个值放入col数组
        result = cursor.fetchall()
        df = pd.DataFrame(list(result))    
    except:
        logger.error("in loadStock,error during visiting stockInfo table")           
    finally:
        cursor.close()
    # 数据表中存在数据，则从数据表中读取     
    if(len(df)>0):        
        df.columns=heads
        return df;
    # 如果没有读取到，则从网站爬取，并插入数据表中
    else:
        logger.info("No data in DB, get from Web")
        df = insertData(stockCode,startDate,endDate)
        return df      

def calBuyPoints(df):
    cnt=0    
    buyDate=''
    while cnt<=len(df)-1:
        if(cnt>=5): # 前几天有误差，从第5天算起
            # 买点规则：股价连续两天下跌，而OBV连续两天上涨
            if df.iloc[cnt-1]['Close']>df.iloc[cnt]['Close'] and df.iloc[cnt-2]['Close']>df.iloc[cnt-1]['Close']:
                logger.debug("calBuyPoints, decrease for 2 days." + df.iloc[cnt]['Date'])
                logger.debug("obv on first day is:" + str(df.iloc[cnt-2]['OBV']))
                logger.debug("obv on second day is:" + str(df.iloc[cnt-1]['OBV']))
                logger.debug("obv on third day is:" + str(df.iloc[cnt]['OBV']))
                if(df.iloc[cnt-1]['OBV']<df.iloc[cnt]['OBV'] and df.iloc[cnt-2]['OBV']<df.iloc[cnt-1]['OBV']):
                    buyDate = buyDate+df.iloc[cnt]['Date'] + ','
        cnt=cnt+1
    return buyDate 

def calSellPoints(df):
    cnt=0    
    sellDate=''
    while cnt<=len(df)-1:
        if(cnt>=5): # 前几天有误差，从第5天算起
            # 卖点规则：股价连续两天上涨，而OBV连续两天下跌
            if df.iloc[cnt-1]['Close']<df.iloc[cnt]['Close'] and df.iloc[cnt-2]['Close']<df.iloc[cnt-1]['Close']:
                logger.debug("calSellPoints, increase for 2 days." + df.iloc[cnt]['Date'])
                logger.debug("obv on first day is:" + str(df.iloc[cnt-2]['OBV']))
                logger.debug("obv on second day is:" + str(df.iloc[cnt-1]['OBV']))
                logger.debug("obv on third day is:" + str(df.iloc[cnt]['OBV']))
                if(df.iloc[cnt-1]['OBV']>df.iloc[cnt]['OBV'] and df.iloc[cnt-2]['OBV']>df.iloc[cnt-1]['OBV']):
                    sellDate = sellDate+df.iloc[cnt]['Date'] + ','
        cnt=cnt+1
    return sellDate 

def draw(request):
    logger.info("start draw")
    # 获取页面参数    
    stockCode = request.POST.get('stockCode')
    logger.info("stockCode is:" + stockCode)    
    startDate = request.POST.get('startDate')
    logger.info("startDate is:" + startDate)
    endDate = request.POST.get('endDate')   
    logger.info("endDate is:" + endDate) 
    # 获取股票数据
    df = loadStock(stockCode,startDate,endDate)
    # 计算OBV值  
    df = calOBV(df)
    
    figure = plt.figure()
    # 创建子图     
    (axPrice, axOBV) = figure.subplots(2, sharex=True)
    # 调用方法，在axPrice子图中绘制K线图 
    candlestick2_ochl(ax = axPrice, 
              opens=df["Open"].values, closes=df["Close"].values,
              highs=df["High"].values, lows=df["Low"].values,
              width=0.75, colorup='red', colordown='green')
    axPrice.set_title("K线图和均线图")    # 设置子图标题
    df['Close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均线')
    df['Close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均线')
    df['Close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均线')
    axPrice.legend(loc='best')      # 绘制图例
    axPrice.set_ylabel("价格（单位：元）")
    axPrice.grid(linestyle='-.')    # 带网格线        
    # 在axOBV子图中绘制OBV图形
    df['OBV'].plot(ax=axOBV,color="blue",label='OBV')
    plt.legend(loc='best') #绘制图例
    plt.rcParams['font.sans-serif']=['SimHei']
    # 在OBV子图上加上负值效果
    plt.rcParams['axes.unicode_minus'] = False
    axOBV.set_ylabel("单位：万手")
    axOBV.set_title("OBV指标图")       # 设置子图的标题
    axOBV.grid(linestyle='-.')         # 带网格线
    # 设置x轴坐标的标签和旋转角度
    major_index=df.index[df.index%5==0]
    major_xtics=df['Date'][df.index%5==0]
    plt.xticks(major_index,major_xtics)
    plt.setp(plt.gca().get_xticklabels(), rotation=30) 
    logger.debug("convert plt to buffer")  
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.close()     
    base64img = base64.b64encode(buffer.getvalue())    
    img = "data:image/png;base64,"+base64img.decode()
    logger.debug("start to Render in stock.html")
    
    buyDate = calBuyPoints(df)
    sellDate = calSellPoints(df)  
    
    return render(request, 'stock.html', {
            'img': img,'stockCode':stockCode,
            'buyDate':buyDate,'sellDate':sellDate})