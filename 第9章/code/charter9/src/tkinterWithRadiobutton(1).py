# !/usr/bin/env python
# coding=utf-8
import tkinter
win = tkinter.Tk()
win.title("单选框")
win.geometry("200x150")
# 创建标签
tkinter.Label(win,text='您目前学的是:').pack()
# 定义选择单选框后执行的操作
def handleSelected():
    text.delete(0.0,tkinter.END)
    text.insert('insert',selectVal.get())
# 创建单选项
selectVal = tkinter.StringVar()
selectVal.set('Python')
pythonSelect = tkinter.Radiobutton(win,text='Python',value='Python',variable=selectVal,command=handleSelected).pack()
javaSelect = tkinter.Radiobutton(win,text='Java',value='Java',variable=selectVal,command=handleSelected).pack()
# 创建多行文本框
text = tkinter.Text(win,width=20,height=3)
text.pack()
win.mainloop()