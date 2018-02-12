# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: check.py
@time: 2017/10/21 下午8:01
"""
import pchong_0
import time
p = 686047550

p = 686064258



# 686051132

while(p<690064626):
    tr,cheng = pchong_0.checkcard(p)
    p = p +1
    print p
    # print cheng