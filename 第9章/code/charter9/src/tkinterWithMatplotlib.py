# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
win = Tk()
win.title("tkinter and matplotlib")
figure = plt.figure()  
# 把用matplotlib绘制的操作定义在方法中，方便调用
def drawPlotOnCancas():      
    ax = figure.add_subplot(111)
    ax.set_title('Matplotlib整合tkinter')
    x = np.array([1,2,3,4,5])
    ax.plot(x, x*x)
    plt.rcParams['font.sans-serif']=['SimHei']
# 在Canvas上显示基于matplotlib的对象
canvs = FigureCanvasTkAgg(figure, win)
canvs.get_tk_widget().pack()
drawPlotOnCancas()
win.mainloop()