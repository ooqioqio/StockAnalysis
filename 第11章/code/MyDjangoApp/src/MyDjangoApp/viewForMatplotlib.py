# !/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
import sys
from io import BytesIO
import base64
import imp
# 以上导入了需要的类库
imp.reload(sys) # 解决导入类库里可能会有的编码问题
def createMatplotlibImg(request):    
    figure = plt.figure()  
    ax = figure.add_subplot(111)
    ax.set_title('django整合matplotlib')
    x = np.array([1,2,3,4,5])
    ax.plot(x, x*x)
    plt.rcParams['font.sans-serif']=['SimHei']
    # 把图形保存为bytes格式，方便传输
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.close() # 关闭plt对象，否则下次调用可能出错    
    base64img = base64.b64encode(buffer.getvalue())    
    img = "data:image/png;base64,"+base64img.decode()    
    return render(request, 'data.html', {
            'img': img
        }) 