import re   # 导入库
numStr = '1c'
numPattern = '^[0-9]+$'         # 匹配数字的正则表达式
if re.match(numPattern,numStr):
    print('All Numbers')
lowCaseStr = 'abc'
strPattern = '^[a-z]+$'         # 匹配小写字母的正则表达式
if re.match(strPattern,lowCaseStr):
    print('All Low Case')
stockPattern='^[6|3|0][0-9]{5}$'    # 匹配沪深A股主板和创业板股票
stockCode='300000'     
if re.match(stockPattern,stockCode):
    print('Is Stock Code')   

myStr = '13785214563'
myPattern = '^1[3|4|5|7|8][0-9]{9}$'
if re.match(myPattern,myStr):
    print('Match')