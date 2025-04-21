# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# 计算RSI的方法，输入参数periodList传入周期列表 
def calRSI(df,periodList):
    # 计算和上一个交易日收盘价的差值
    df['diff'] = df["Close"]-df["Close"].shift(1) 
    df['diff'].fillna(0, inplace = True)    
    df['up'] = df['diff']
    # 过滤掉小于0的值
    df['up'][df['up']<0] = 0
    df['down'] = df['diff']
    # 过滤掉大于0的值
    df['down'][df['down']>0] = 0
    # 通过for循环，依次计算periodList中不同周期的RSI等值
    for period in periodList:
        df['upAvg'+str(period)] = df['up'].rolling(period).sum()/period
        df['upAvg'+str(period)].fillna(0, inplace = True)
        df['downAvg'+str(period)] = abs(df['down'].rolling(period).sum()/period)
        df['downAvg'+str(period)].fillna(0, inplace = True)
        df['RSI'+str(period)] = 100 - 100/((df['upAvg'+str(period)]/df['downAvg'+str(period)]+1))
    return df
filename='D:\\stockData\ch10\\6005842018-09-012019-05-31.csv'
df = pd.read_csv(filename,encoding='gbk')
list = [6,12,24]    # 周期列表
# 调用方法计算RSI
stockDataFrame = calRSI(df,list) 
cnt=0    
sellDate=''
while cnt<=len(stockDataFrame)-1:
    if(cnt>=30):    # 前几天有误差，从第30天算起
        try:        
            # 规则1：这天RSI6高于80
            if stockDataFrame.iloc[cnt]['RSI6']<80:
                # 规则2.1：当天RSI6下穿RSI12
                if  stockDataFrame.iloc[cnt]['RSI6']<stockDataFrame.iloc[cnt]['RSI12'] and stockDataFrame.iloc[cnt-1]['RSI6']>stockDataFrame.iloc[cnt-1]['RSI12']:
                    sellDate = sellDate+stockDataFrame.iloc[cnt]['Date'] + ','
                    # 规则2.2：当天RSI6下穿RSI24
                if  stockDataFrame.iloc[cnt]['RSI6']<stockDataFrame.iloc[cnt]['RSI24'] and stockDataFrame.iloc[cnt-1]['RSI6']>stockDataFrame.iloc[cnt-1]['RSI24']:
                    if sellDate.index(stockDataFrame.iloc[cnt]['Date']) == -1:
                        sellDate = sellDate+stockDataFrame.iloc[cnt]['Date'] + ','
        except:
            pass                
    cnt=cnt+1
print(sellDate)    
def sendMail(username,pwd,from_addr,to_addr,msg):
    try:
        smtp = smtplib.SMTP() 
        smtp.connect('smtp.163.com') 
        smtp.login(username, pwd) 
        smtp.sendmail(from_addr,to_addr, msg) 
        smtp.quit()
    except Exception as e:  
        print(str(e))
def buildMail(HTMLContent,subject,showFrom,showTo,attachfolder,attachFileName):
    message = MIMEMultipart()
    body = MIMEText(HTMLContent, 'html', 'utf-8')
    message.attach(body)
    message['Subject'] = subject
    message['From'] = showFrom
    message['To'] = showTo
    imageFile = MIMEImage(open(attachfolder+attachFileName, 'rb').read())
    imageFile.add_header('Content-ID', attachFileName)
    imageFile['Content-Disposition'] = 'attachment;filename="'+attachFileName+'"'
    message.attach(imageFile)
    return message 
subject='RSI卖点分析'
attachfolder='D:\\stockData\\ch10\\'
attachFileName='600584RSI.png'
HTMLContent = '<html><head></head><body>'\
 '卖点日期' + sellDate + \
 '<img src="cid:'+attachFileName+'"/>'\
 '</body></html>'
message = buildMail(HTMLContent,subject,'hsm_computer@163.com','hsm_computer@163.com',attachfolder,attachFileName) 
sendMail('hsm_computer','xxx','hsm_computer@163.com','hsm_computer@163.com',message.as_string())          