# !/usr/bin/env python
# coding=utf-8
import tkinter
win = tkinter.Tk()
win.title("复选框")
win.geometry("150x160")
# 添加Label标签
tkinter.Label(win,text='我已经掌握的编程语言').pack(anchor=tkinter.W)
# 单击复选框后触发的函数
def handleFunc():
    msg = ''
    # 选中为True，不选为False，下同
    if pythonSelected.get() == True: 
        msg += pythonCheckButton.cget('text');
        msg+='\n'        
    if javaSelected.get() == True:
        msg += javaCheckBotton.cget('text')
        msg+='\n'
    if goSelected.get() == True:
        msg += goCheckBotton.cget('text')
        msg += "\n"    
    text.delete(0.0,tkinter.END)
    text.insert('insert',msg)
# 创建复选框
pythonSelected = tkinter.BooleanVar()
pythonCheckButton = tkinter.Checkbutton(win,text='Python',variable=pythonSelected,command=handleFunc)
pythonCheckButton.pack(anchor=tkinter.W)
javaSelected = tkinter.BooleanVar()
javaCheckBotton = tkinter.Checkbutton(win,text='Java',variable=javaSelected,command=handleFunc)
javaCheckBotton.pack(anchor=tkinter.W)
goSelected = tkinter.BooleanVar()
goCheckBotton = tkinter.Checkbutton(win,text='Go',variable=goSelected,command=handleFunc)
goCheckBotton.pack(anchor=tkinter.W)
# 创建一个多行文本框
text = tkinter.Text(win,width=20,height=5)
text.pack(anchor=tkinter.W)
win.mainloop()