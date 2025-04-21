import tushare as ts
def saveStockByTS(code):    # 定义获取并保存指定股票交易数据的方法
    start='2019-01-01'
    end='2019-01-31'
    ts.get_hist_data(code=code,start=start,end=end).to_csv('d:\\stockData\\ch5\\'+code+'.csv',columns=['open','high','close','low','volume'])
# 开始调用
code='600895'       # 股票“张江高科”
saveStockByTS(code)
# 也可以去掉下面的注释，在获取股票代码的同时获取该股票的信息
# stockList=ts.get_stock_basics()
# for code in stockList.index:
    # saveStockByTS(code)