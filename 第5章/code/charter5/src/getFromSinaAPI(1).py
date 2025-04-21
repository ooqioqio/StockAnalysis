# coding=utf-8
import requests
import re
# 定义爬取打印和保存数据的方法
def printAndSaveStock(code):
    url = 'http://hq.sinajs.cn/list=' + code
    response = requests.get(url).text    
    rule = r'"(.*?)"'       # 设置截取字符串的规则
    result = re.findall(rule, response)    
    print(result[0])
    filename = 'D:\\stockData\\ch5\\'+code+".csv"
    f = open(filename,'w')
    # findall方法返回的是列表，这里第0号索引存放所需的内容
    f.write(result[0])  # 写文件
    f.close()           # 关闭文件
# 爬取张江高科和中国国贸这两只股票的交易数据
codes = ['sh600895', 'sh600007']
for code in codes:
    printAndSaveStock(code)