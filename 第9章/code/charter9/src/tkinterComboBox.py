# !/usr/bin/env python
# coding=utf-8
import tkinter as tk
from tkinter import ttk
win = tk.Tk() 
win.title("下拉框")    # 添加标题
tk.Label(win, text="选择编程语言").grid(column=0, row=0)    # 添加标签  
# 创建下拉框 
comboboxVal = tk.StringVar() 
combobox = ttk.Combobox(win, width=12, textvariable=comboboxVal) 
combobox['values'] = ('Python', 'Java', '.NET','go')        # 设置下拉列表框的值 
combobox.grid(column=1, row=0)      # 设置其在界面中出现的位置，column代表列，row 代表行 
combobox.current(0)    # 设置下拉列表框的默认值 
# 清空并插入文本框的内容
def handle(): 
    text.delete(0,tk.END)
    text.insert(0,combobox.get()) 
# 创建按钮 
button = tk.Button(win, text="选择", width=12,command=handle)
button.grid(column=1, row=1) 
# 创建文本框 
val = tk.StringVar()  
text = tk.Entry(win, width=12, textvariable=val)    # 创建文本框
text.grid(column=0, row=1)
text.focus()    # 默认设置焦点（光标）在文本框中
win.mainloop()  # 开启主循环以监听事件