# !/usr/bin/env python
# coding=utf-8
import os,shutil    # 通过import导入两个库
def moveFile(src,dest):
    if not os.path.isfile(src):
        print("File not exist!" + src)
    else:
        fpath=os.path.split(dest)[0]   # 获取路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)         # 如果路径不存在，则创建
        shutil.move(src,dest)          # 移动文件
        print('Finished Moving')
def copyFile(src,dest):
    if not os.path.isfile(src):
        print("File not exist!" + src)
    else:
        fpath=os.path.split(dest)[0]    # 获取路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)          # 创建路径
        shutil.copyfile(src,dest)       # 复制文件
        print('Finished Copying')
# 调用方法
srcForCopy='c:\\1\\python.txt'
destForCopy='c:\\1\\python1.txt'
copyFile (srcForCopy,destForCopy)
srcForMove='c:\\1\\python.txt'
destForMove='c:\\1\\python2.txt'
moveFile (srcForMove,destForMove)

