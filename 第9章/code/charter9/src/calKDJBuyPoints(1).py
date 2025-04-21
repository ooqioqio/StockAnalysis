# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader
from mpl_finance import candlestick2_ochl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
import tkinter.messagebox
# 计算KDJ
def calKDJ(df):
    df['MinLow'] = df['Low'].rolling(9, min_periods=9).min()
    # 填充NaN数据
    df['MinLow'].fillna(value = df['Low'].expanding().min(), inplace = True) 
    df['MaxHigh'] = df['High'].rolling(9, min_periods=9).max()
    df['MaxHigh'].fillna(value = df['High'].expanding().max(), inplace = True)    
    df['RSV'] = (df['Close'] - df['MinLow']) / (df['MaxHigh'] - df['MinLow']) * 100
    for i in range(len(df)):
        if i==0:    # 第一天
            df.ix[i,'K']=50
            df.ix[i,'D']=50
        if i>0:
            df.ix[i,'K']=df.ix[i-1,'K']*2/3 + 1/3*df.ix[i,'RSV']
            df.ix[i,'D']=df.ix[i-1,'D']*2/3 + 1/3*df.ix[i,'K']            
        df.ix[i,'J']=3*df.ix[i,'K']-2*df.ix[i,'D']  
    return df
# 绘制KDJ线
def drawKDJAndKLine(stockCode,startDate,endDate):
    filename='D:\\stockData\ch9\\'+stockCode+startDate+endDate+'.csv'
    getStockDataFromAPI(stockCode,startDate,endDate)
    df = pd.read_csv(filename,encoding='gbk')
    stockDataFrame = calKDJ(df)
    # 创建子图     
    (axPrice, axKDJ) = figure.subplots(2, sharex=True)
    # 调用方法，在第axPrice子图中绘制K线图 
    candlestick2_ochl(ax = axPrice, 
                  opens=stockDataFrame["Open"].values, closes=stockDataFrame["Close"].values,
                  highs=stockDataFrame["High"].values, lows=stockDataFrame["Low"].values,
                  width=0.75, colorup='red', colordown='green')
    axPrice.set_title("K线图和均线图")    # 设置子图标题
    stockDataFrame['Close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均线')
    stockDataFrame['Close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均线')
    stockDataFrame['Close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均线')
    axPrice.legend(loc='best')      # 绘制图例
    axPrice.set_ylabel("价格（单位：元）")
    axPrice.grid(linestyle='-.')    # 带网格线        
    # 在axKDJ子图中绘制KDJ
    stockDataFrame['K'].plot(ax=axKDJ,color="blue",label='K')
    stockDataFrame['D'].plot(ax=axKDJ,color="green",label='D')
    stockDataFrame['J'].plot(ax=axKDJ,color="purple",label='J')
    plt.legend(loc='best')          # 绘制图例
    plt.rcParams['font.sans-serif']=['SimHei']       
    axKDJ.set_title("KDJ图")        # 设置子图的标题
    axKDJ.grid(linestyle='-.')      # 带网格线
    # 设置x轴坐标的标签和旋转角度
    major_index=stockDataFrame.index[stockDataFrame.index%5==0]
    major_xtics=stockDataFrame['Date'][stockDataFrame.index%5==0]
    plt.xticks(major_index,major_xtics)
    plt.setp(plt.gca().get_xticklabels(), rotation=30) 
# 从API中获取股票数据
def getStockDataFromAPI(stockCode,startDate,endDate):
    try:
        # 给股票代码加ss前缀来获取上证股票的数据
        stock = pandas_datareader.get_data_yahoo(stockCode+'.ss',startDate,endDate)
        if(len(stock)<1):
            # 如果没取到数据，则抛出异常 
            raise Exception()
        # 删除最后一行，因为get_data_yahoo会多取一天的股票交易数据
        stock.drop(stock.index[len(stock)-1],inplace=True)  # 在本地留份csv
        filename='D:\\stockData\ch9\\'+stockCode+startDate+endDate+'.csv'
        stock.to_csv(filename)                
    except Exception as e:
        print('Error when getting the data of:' + stockCode)
        print(repr(e))
# 设置tkinter窗口
win = tkinter.Tk()
win.geometry('625x600')     # 设置大小
win.title("K线均线整合KDJ")
# 放置控件
tkinter.Label(win,text='股票代码：').place(x=10,y=20)
tkinter.Label(win,text='开始时间：').place(x=10,y=50)
tkinter.Label(win,text='结束时间：').place(x=10,y=80)
stockCodeVal = tkinter.StringVar()
startDateVal = tkinter.StringVar()
endDateVal = tkinter.StringVar()
stockCodeEntry = tkinter.Entry(win,textvariable=stockCodeVal)
stockCodeEntry.place(x=70,y=20)
stockCodeEntry.insert(0,'600640')
startDateEntry = tkinter.Entry(win,textvariable=startDateVal)
startDateEntry.place(x=70,y=50)
startDateEntry.insert(0,'2019-01-01')
endDateEntry = tkinter.Entry(win,textvariable=endDateVal)
endDateEntry.place(x=70,y=80)
endDateEntry.insert(0,'2019-05-31')
def draw():     # 绘制按钮的处理函数
    plt.clf()   # 先清空所有在plt上的图形   
    stockCode=stockCodeVal.get()
    startDate=startDateVal.get()    
    endDate=endDateVal.get()
    drawKDJAndKLine(stockCode,startDate,endDate)
    canvas.draw()  
tkinter.Button(win,text='绘制',width=12,command=draw).place(x=200,y=50)
def reset():
    stockCodeEntry.delete(0,tkinter.END)
    stockCodeEntry.insert(0,'600640')
    startDateEntry.delete(0,tkinter.END)
    startDateEntry.insert(0,'2019-01-01')
    endDateEntry.delete(0,tkinter.END)
    endDateEntry.insert(0,'2019-05-31')
    plt.clf()
    canvas.draw() 
tkinter.Button(win,text='重置',width=12,command=reset).place(x=200,y=80)
# 以对话框的形式输出买点
def printBuyPoints():
    stockCode=stockCodeVal.get()
    startDate=startDateVal.get()    
    endDate=endDateVal.get()    
    filename='D:\\stockData\ch9\\'+stockCode+startDate+endDate+'.csv'
    getStockDataFromAPI(stockCode,startDate,endDate)
    df = pd.read_csv(filename,encoding='gbk')
    stockDf = calKDJ(df)
    cnt=0
    buyDate=''
    while cnt<=len(stockDf)-1:
        if(cnt>=5):     # 略过前几天的误差
            #规则1：前一天J值大于10，当天J值小于10，是买点、        
            if stockDf.iloc[cnt]['J']<10 and stockDf.iloc[cnt-1]['J']>10:
                buyDate = buyDate+stockDf.iloc[cnt]['Date'] + ','
                cnt=cnt+1
                continue 
            # 规则2：K,D均在20之下，出现K线上穿D线的金叉现象
            # 规则1和规则2是“或”的关系，所以当满足规则1时直接continue
            if stockDf.iloc[cnt]['K']>stockDf.iloc[cnt]['D'] and stockDf.iloc[cnt-1]['D']>stockDf.iloc[cnt-1]['K']:
                # 满足上穿条件后再判断K和D均小于20                
                if stockDf.iloc[cnt]['K']< 20 and stockDf.iloc[cnt]['D']<20:
                    buyDate = buyDate + stockDf.iloc[cnt]['Date'] + ','
        cnt=cnt+1            
    # 完成后，通过对话框的形式显示买入日期
    tkinter.messagebox.showinfo('提示买点',buyDate)
tkinter.Button(win,text='计算买点',width=12,command=printBuyPoints).place(x=300,y=50)
# 开始整合figure和win
figure = plt.figure()
canvas = FigureCanvasTkAgg(figure, win)
canvas.get_tk_widget().config(width=575,height=500)
canvas.get_tk_widget().place(x=0,y=100)
win.mainloop()