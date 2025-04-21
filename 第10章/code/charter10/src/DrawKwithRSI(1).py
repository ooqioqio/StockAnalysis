# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl
from matplotlib.ticker import MultipleLocator
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
figure = plt.figure()
# 创建子图     
(axPrice, axRSI) = figure.subplots(2, sharex=True)
# 调用方法，在axPrice子图中绘制K线图 
candlestick2_ochl(ax = axPrice, 
              opens=df["Open"].values, closes=df["Close"].values,
              highs=df["High"].values, lows=df["Low"].values,
              width=0.75, colorup='red', colordown='green')
axPrice.set_title("K线图和均线图")    # 设置子图标题
stockDataFrame['Close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均线')
stockDataFrame['Close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均线')
stockDataFrame['Close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均线')
axPrice.legend(loc='best')      # 绘制图例
axPrice.set_ylabel("价格（单位：元）")
axPrice.grid(linestyle='-.')    # 带网格线        
# 在axRSI子图中绘制RSI图形
stockDataFrame['RSI6'].plot(ax=axRSI,color="blue",label='RSI6')
stockDataFrame['RSI12'].plot(ax=axRSI,color="green",label='RSI12')
stockDataFrame['RSI24'].plot(ax=axRSI,color="purple",label='RSI24')
plt.legend(loc='best')          # 绘制图例
plt.rcParams['font.sans-serif']=['SimHei']       
axRSI.set_title("RSI图")        # 设置子图的标题
axRSI.grid(linestyle='-.')      # 带网格线
# 设置x轴坐标的标签和旋转角度
major_index=stockDataFrame.index[stockDataFrame.index%7==0]
major_xtics=stockDataFrame['Date'][stockDataFrame.index%7==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.savefig('D:\\stockData\ch10\\600584RSI.png')         
# 发送邮件
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

subject='RSI效果图'
attachfolder='D:\\stockData\\ch10\\'
attachFileName='600584RSI.png'
HTMLContent = '<html><head></head><body>'\
 '<img src="cid:'+attachFileName+'"/>'\
 '</body></html>'
message = buildMail(HTMLContent,subject,'hsm_computer@163.com','hsm_computer@163.com',attachfolder,attachFileName) 
sendMail('hsm_computer','xxx','hsm_computer@163.com','hsm_computer@163.com',message.as_string())  
# 最后再绘制
plt.show()