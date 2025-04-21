# !/usr/bin/env python
# coding=utf-8
# 演示while的用法

number = 1
while number < 10:
    number += 1
    if not number % 2 == 0: # 不是双数时则跳过本轮循环
        continue
    else: 
        print (number)      # 输出双数2、4、6、8、10
#以上输出2，4，6,8,10这些偶数 
 
number = 1
while True:              # 条件是True表示一直执行 
    print (number)         # 输出1到5
    number = number+1
    if number > 5:       # 当i大于5时跳离循环体
        break
# 以上输出1,2,3,4,5

