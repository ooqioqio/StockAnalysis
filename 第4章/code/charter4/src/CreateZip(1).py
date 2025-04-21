# !/usr/bin/env python
# coding=utf-8
import zipfile,os   # 导入两个库
zip=zipfile.ZipFile('c:\\1.zip', 'w')   # 指定压缩后的文件名
try:
    for curPath, subFolders, files in os.walk('c:\\1'):
        for file in files:              # 压缩所有的文件
            print(os.path.join(curPath, file))        
            zip.write(os.path.join(curPath, file))
except:
    print("Error When Creating Zip File")
finally:                
    zip.close()