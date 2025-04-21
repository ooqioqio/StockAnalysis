# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import numpy as np
s = np.arange(1,6,1)
print(s)    # 输出[1 2 3 4 5]
print(pd.Series(s).rolling(3).mean())