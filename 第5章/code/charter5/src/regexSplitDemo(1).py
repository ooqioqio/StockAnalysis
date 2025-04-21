# coding=utf-8
import re
# 以等号分隔，输出等号两边的字符串['content', 'Hello World']
print(re.split('=','content=Hello World')) 
# 输出等号左边的字符串content
print(re.split('=','content=Hello World')[0]) 
# 输出等号右边的字符串Hello World
print(re.split('=','content=Hello World')[1]) 

str = 'content=code:(600001),price:(20)'
pattern = re.compile(r'[(](.*?)[)]')
# 输出括号内的所有内容['600001', '20'] 
print(re.findall(pattern, str))

# 获取<>之间的所有内容
rule = r'<(.*?)>'
result = re.findall(rule, 'content=<123>')
print(result)   # 输出['123']

# 获取引号之间的内容
rule = r'"(.*?)"'
result = re.findall(rule, 'content="456"')
print(result)   # 输出['456']

# 用逗号分隔
str='600001,10,12,15'
item=re.split(',',str) 
print(item)     # 输出['600001', '10', '12', '15']