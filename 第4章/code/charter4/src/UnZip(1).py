# !/usr/bin/env python
# coding=utf-8
import shutil,zipfile
# shutil.unpack_archive('c:\\1.zip','c:\\2')
f = zipfile.ZipFile("c:\\1.zip",'r')
for file in f.namelist():
    f.extract(file,"c:\\2") 
f.close()    