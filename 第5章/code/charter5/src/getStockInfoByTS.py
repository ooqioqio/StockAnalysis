# coding=utf-8
import tushare as ts    # 导入库
# 指定保存的文件名
fileName='D:\\stockData\\ch5\\stockListByTs.csv'
stockList=ts.get_stock_basics()     # 调用方法得到信息
print(stockList)        # 在控制台打印
stockList.to_csv(fileName,encoding='gbk')   # 保存到csv中