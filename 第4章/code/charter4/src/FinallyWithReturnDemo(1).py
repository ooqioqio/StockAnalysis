# !/usr/bin/env python
# coding=utf-8
def funcWithFinally():
    try:
        print("In Try")
        return "Return in Try"
    finally:
        print("In Finally") 
        #return "Return in Finally"
print(funcWithFinally())     