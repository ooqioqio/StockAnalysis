# !/usr/bin/env python
# coding=utf-8

# 定义冒泡排序的函数
def SortFunc(numArray):
    # 初始化一个变量 loopTimes，用于记录冒泡排序的循环次数
    # 初始值为 0，随着排序的进行，该值会逐渐增加
    loopTimes = 0; 
    # 外层循环控制排序的轮数，总共需要进行 len(numArray) - 1 轮排序
    # 因为每一轮排序都会将当前未排序部分的最大元素移动到末尾，所以最后一个元素无需再进行比较
    while loopTimes < len(numArray) - 1: 
        # 内层循环用于比较相邻元素并进行交换
        # 每一轮排序后，末尾的元素已经是有序的，所以不需要再比较，因此范围是 len(numArray) - loopTimes - 1
        for index in range(len(numArray) - loopTimes - 1):
            # 比较相邻的两个元素，如果前一个元素大于后一个元素
            if numArray[index] > numArray[index + 1]:
                # 使用临时变量 tmp 保存前一个元素的值
                tmp = numArray[index]
                # 将后一个元素的值赋给前一个元素
                numArray[index] = numArray[index + 1]
                # 将临时变量 tmp 中保存的值赋给后一个元素，完成交换
                numArray[index + 1] = tmp 
        # 每完成一轮排序，循环次数加 1
        loopTimes = loopTimes + 1       
        
    # 排序完成后，返回排序好的数组
    print(loopTimes) 
    return numArray
   
unSortedNums = [10,12,48,7,5,3,14]
print (SortFunc(unSortedNums))
