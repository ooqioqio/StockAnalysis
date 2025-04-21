# !/usr/bin/env python
# coding=utf-8
# 通过lambda表达式定义了一个匿名函数
add = lambda a,b,c:a+b+c
print(add(1,2,3)) # 输出6
# 计算奇数
numbers = [1, 3, 6, 7, 10,11]   
# 与filter整合使用
numbers = filter(lambda input: input%2!=0, numbers)
print numbers #[1, 3, 7, 11]
numbers = [2, 3, 4]
# 与map整合使用
numbers = map(lambda x: x*x, numbers)
print numbers #[4, 9, 16]
# 与reduce整合使用
numbers = [1,2,3,4,5]   
sum = reduce(lambda x, y: x + y, numbers)
print sum # 输出15
# 与sorted整合使用
numbers = [1,-2, 3, -4,5]
numbers = sorted(numbers, lambda x, y: abs(y)-abs(x))
print numbers # [5, -4, 3, -2, 1]