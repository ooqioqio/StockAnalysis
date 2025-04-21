# coding=utf-8
import pandas_datareader
stockCodeList = []
stockCodeList.append('600007.ss')  # 沪股“中国国贸” 
stockCodeList.append('000001.sz')  # 深股“平安银行”
stockCodeList.append('2318.hk')    # 港股“中国平安”
stockCodeList.append('IBM')        # 美股，IBM，直接输入股票代码不带后缀

for code in stockCodeList:
    # 为了演示，只取一天的交易数据
    stock = pandas_datareader.get_data_yahoo(code,'2019-01-02','2019-01-02')
    print(stock)