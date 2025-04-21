# !/usr/bin/env python
# coding=utf-8
try:
    filename = 'c:\\1\\myFile.txt'
    f = open(filename,'a')
    f.write('Hello,')
    f.write('Python!')
except:
    print("Error when writing the file:" + filename)
finally:
    try:            
        f.close()
    except:
        print("No Need to close file:" + filename)        