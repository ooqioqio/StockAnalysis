# !/usr/bin/env python
# coding=utf-8
import pandas as pd
# 从文件中读取数据
df = pd.read_csv('D:/stockData/ch7/600895.csv',encoding='gbk')
maIntervalList = [3,5,10]
# 虽然在后文中只用到了5日均线，但这里演示设置3种均线
for maInterval in maIntervalList:
    df['MA_' + str(maInterval)] = df['Close'].rolling(window=maInterval).mean()
cnt=0    
while cnt<=len(df)-1:
    try:
        # 规则1，收盘价连续三天下跌
        if df.iloc[cnt]['Close']>df.iloc[cnt+1]['Close'] and df.iloc[cnt+1]['Close']>df.iloc[cnt+2]['Close']:
            # 规则2，5日均线连续三天下跌
            if df.iloc[cnt]['MA_5']>df.iloc[cnt+1]['MA_5'] and df.iloc[cnt+1]['MA_5']>df.iloc[cnt+2]['MA_5']:
                #规则3，第3天收盘价下穿5日均线
                if df.iloc[cnt+1]['MA_5']<df.iloc[cnt]['Close'] and df.iloc[cnt+2]['MA_5']>df.iloc[cnt+1]['Close']:     
                    print("Sell Point on:" + df.iloc[cnt]['Date'])
    except: # 有几天是没有5日均线的，所以用except处理异常
        pass                
    cnt=cnt+1