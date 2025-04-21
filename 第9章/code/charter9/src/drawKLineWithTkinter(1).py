# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from mpl_finance import candlestick2_ochl
import tkinter
win = tkinter.Tk()
df = pd.read_csv('D:/stockData/ch6/600895.csv',encoding='gbk',index_col=0)
win.title("tkinter整合matplotlib")
figure = plt.figure()
canvas = FigureCanvasTkAgg(figure, win)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=2)  
# 把用matplotlib绘制的操作定义在方法中，方便调用
def drawKLineOnCancas():   
    plt.clf() #先清空所有在plt上的图形   
    ax = figure.add_subplot(111)
    ax.set_title('600895张江高科的K线图')
    ax = figure.add_subplot(111)
    # 调用方法绘制K线图 
    candlestick2_ochl(ax = ax, 
                  opens=df["Open"].values, closes=df["Close"].values,
                  highs=df["High"].values, lows=df["Low"].values,
                  width=0.75, colorup='red', colordown='green')
    df['Close'].rolling(window=3).mean().plot(color="red",label='3日均线')
    df['Close'].rolling(window=5).mean().plot(color="blue",label='5日均线')
    df['Close'].rolling(window=10).mean().plot(color="green",label='10日均线')
    plt.legend(loc='best')  # 绘制图例
    plt.xticks(range(len(df.index.values)),df.index.values,rotation=30 ) 
    ax.grid(True)           # 带网格
    plt.rcParams['font.sans-serif']=['SimHei']
    canvas.draw() 

button =tkinter.Button(win, text='开始绘制', width=10,command=drawKLineOnCancas).grid(row=1,column=0,columnspan=3)
def clearCanvas():
    plt.clf()  
    canvas.draw() 
button =tkinter.Button(win, text='清空', width=10,command=clearCanvas).grid(row=1,column=1,columnspan=3)
win.mainloop()