# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: check.py
@time: 2017/10/21 下午8:01
"""
import pchong_0
import re_test
import get_szt_money_with_api as fun
import time
p = 686047550

p = 686064258

p = 686076027

p = 686094281

# mys = re_test.mysql_dbs('agent')

# 686051132
# l = mys.get_id()[-1:][0][0]+1

l = 686098765

while 1 :
    tr,cheng = pchong_0.checkcard(l)
    if tr == 1 :
        print(cheng)
        # mys.insert(cheng)
        # if float(cheng[2]) > 80:
            # mys.insert(cheng)

    l = l +1
    if l%8 == 0:
        time.sleep(2)
    if l == 100:
        break
    print l
    # print cheng

# while 1 :
#     cheng = fun.getinfo(p + l)
#
#     # mys.insert(cheng)
#     print cheng
#
#     l = l +1
#     if l == 100:
#         break
#     print l
#     # print cheng