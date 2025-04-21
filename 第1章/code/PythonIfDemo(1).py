# !/usr/bin/env python
# coding=utf-8

# 判断闰年
year = 2028
# year = 2020
if (year % 4 == 0) and (year % 100 != 0):
    print(f"{year}是闰年")
elif year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

