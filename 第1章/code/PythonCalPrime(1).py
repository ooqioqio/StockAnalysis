# !/usr/bin/env python
# coding=utf-8

# 定义一个名为 printPrime 的函数，用于打印出从 2 到 maxNum 之间的所有质数
# 参数 maxNum: 一个整数，表示查找质数的上限
def printPrime(maxNum):
    # 初始化一个空列表 num，用于存储找到的质数
    num = []
    # 初始化当前要检查的数字为 2，因为 2 是最小的质数
    currentNum = 2
    # 外层循环，遍历从 2 到 maxNum 的所有数字
    for currentNum in range(2, maxNum + 1):
        # 初始化除数为 2，因为质数是大于 1 且只能被 1 和自身整除的数
        devidedNum = 2
        # 内层循环，检查 currentNum 是否能被 2 到 currentNum-1 之间的任何数整除
        for devidedNum in range(2, currentNum+1):
            # 如果 currentNum 能被 devidedNum 整除，说明它不是质数，跳出内层循环
            if (currentNum % devidedNum == 0):
                break
        # 如果内层循环正常结束（即没有执行 break 语句），此时 devidedNum 会等于 currentNum
        # 这意味着 currentNum 不能被 2 到 currentNum-1 之间的任何数整除，是质数
        if currentNum == devidedNum:   
            # 把质数加入到列表 num 里
            num.append(currentNum) 
        #print(num)          
    # 打印存储所有质数的列表
    print(num)
       
# 绿色 ANSI 转义码
GREEN = '\033[92m'
# 重置 ANSI 转义码
RESET = '\033[0m'
print(f"{GREEN}", end="")
printPrime(1014)
print(f"{RESET}", end="")
