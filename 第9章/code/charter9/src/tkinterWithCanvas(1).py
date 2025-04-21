# !/usr/bin/env python
# coding=utf-8
import tkinter as tk
win = tk.Tk()
win.title('Cavas画布')    # 设置窗口标题
win.geometry("550x350")
canvas = tk.Canvas(win,background='white',width=500,height=300)
canvas.pack()
# 绘制直线
canvas.create_line((0, 0), (60, 60), width=2, fill="red")
# 绘制圆弧
canvas.create_arc((210, 210), (280, 280),fill='yellow',width=3)
# 绘制矩形
canvas.create_rectangle(75, 75, 120, 120, fill='green', width=2)
# 显示文字
canvas.create_text(350, 200,text='演示文字效果')
# 绘制圆或椭圆，取决于外接矩形
canvas.create_oval(150, 150, 200, 200,fill='red')
# 连接由参数指定的点，绘制多边形
point = [(280, 260), (300, 200), (350, 220),(400,280)]
canvas.create_polygon(point, outline='green', fill='yellow')
win.mainloop()