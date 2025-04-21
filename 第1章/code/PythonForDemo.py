# !/usr/bin/env python
# coding=utf-8
# 演示for的用法

languages = ["Java", "Go", "C++", "Python", "C#"]
for tool in languages:
    if tool == "C++":
        continue # 不会输出C++
    if tool == "Python":
        print("我正在学Python。")
        break
    print (tool)
# 输出了Java，Go，我正在学Python，没有输出C#

