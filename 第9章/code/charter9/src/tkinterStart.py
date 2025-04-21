# !/usr/bin/env python
# coding=utf-8
import tkinter
import tkinter.messagebox 
loginWin = tkinter.Tk()
loginWin.geometry('220x120')    # 设置大小
loginWin.title('登录窗口')      # 设置窗口标题
# 放置两个Label标签
tkinter.Label(loginWin,text='用户名：').place(x=10,y=20)
tkinter.Label(loginWin,text='密 码：').place(x=10,y=50)
userVal = tkinter.StringVar()
pwdVal = tkinter.StringVar()
# Entry是用来接受字符串的控件
userEntry = tkinter.Entry(loginWin,textvariable=userVal)
userEntry.place(x=65,y=20)
pwdEntry = tkinter.Entry(loginWin,textvariable=pwdVal,show='*')  # 用*号代替输入文字
pwdEntry.place(x=65,y=50)
def check():    # 定义登录按钮的处理函数（即定义单击登录按钮时触发的方法）
    userName=userVal.get()
    pwd=pwdVal.get()
    print('用户名:'+ userName)
    print('密码:'+pwd)
    if(userName=='python' and  pwd =='kdj'):
        tkinter.messagebox.showinfo('提示','登录成功') 
    else:           
        tkinter.messagebox.showinfo('提示','登录失败')
tkinter.Button(loginWin,text='登录',width=12,command=check).place(x=10,y=85)
tkinter.Button(loginWin,text='退出',width=12,command=loginWin.quit).place(x=120,y=85)
tkinter.mainloop()