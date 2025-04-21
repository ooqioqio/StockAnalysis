# !/usr/bin/env python
# coding=utf-8
# 以列表方式定义Mike和Tom两个人的账户
accountsInfoList = [{'name': 'Mike', 'balance': 100,'stockList':['600123','600158']}, {'name': 'Tom', 'balance': 200,'stockList':['600243','600558']} ]
# 通过for循环，依次输出列表中的元素
for item in accountsInfoList:
    print item['name'],
    print item['balance'],
    print item['stockList']
# 以字典的方式定义
accountInfoDict={ 'Peter':{'balance': 100,'stockList':['600123','600158'] }, 'Tom': { 'balance': 200,'stockList':['600243','600558']} }
# 输出{'balance': 100, 'stockList': ['600123', '600158']}
print(accountInfoDict.get('Peter'))
PeterAccount={ 'Peter':{'balance': 200,'stockList':['600223','600158',600458] }}
accountInfoDict.update(PeterAccount)
print(accountInfoDict.get('Peter')) # 能看到更新后的内容
JohnAccount={ 'John':{'balance': 200,'stockList':[] }}
accountInfoDict.update(JohnAccount)
# 利用双层循环打印
for name,account in accountInfoDict.items():
    print ("name is %s:"%(name)),   # 输出name后不换行
    for key,value in account.items():
        print value,
    print # 输完一个人的信息后换行