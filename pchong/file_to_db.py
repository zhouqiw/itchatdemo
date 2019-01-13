# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: get_szt_money_with_api.py
@time: 2018/12/26 下午11:13
"""

import sys
import json
import time

import re_test

reload(sys)
sys.setdefaultencoding('utf8')
s = ''




def tast():
    mys = re_test.mysql_dbs('agent')

    n = 0
    s = time.time()

    with open('4.txt','r') as f :
        lines = f.readlines()
        for i in lines:
            rs = json.loads(i)
            # print n
            # print rs
            if rs["code"] == 0:
            # rs["data"]["card_number"], rs["data"]["balance_time"], rs["data"]["card_balance"]
                print(rs["data"]["card_number"], rs["data"]["balance_time"], rs["data"]["card_balance"].replace('元', ''))
                mys.insert_1(rs["data"]["card_number"], rs["data"]["balance_time"], rs["data"]["card_balance"].replace('元', ''))
            n = n+1
    print 'hangshu:{0}'.format(n)

    print time.time()-s


    # s = time.time()
    # while i < 800:
    #     a, b ,c = getinfo(l+i)
    #     mys.insert_1(a,b,c.replace('元',''))
    #     i = i + 1
    # print time.time()-s


if __name__ == '__main__':
    tast()
    #
    # while 1 :
    #
    #     try:
    #         n = 0
    #         fname = '3.txt'
    #         last_line = ''
    #         with open(fname, 'r') as f:  # 打开文件
    #             first_line = f.readline()  # 读第一行
    #             off = -50  # 设置偏移量
    #             while True:
    #                 f.seek(off, 2)  # seek(off, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
    #                 lines = f.readlines()  # 读取文件指针范围内所有行
    #                 if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
    #                     last_line = lines[-1]  # 取最后一行
    #                     break
    #                 # 如果off为50时得到的readlines只有一行内容，那么不能保证最后一行是完整的
    #                 # 所以off翻倍重新运行，直到readlines不止一行
    #                 off *= 2
    #
    #             # print '文件' + fname + '第一行为：' + first_line
    #             # print '文件' + fname + '最后一行为：' + last_line
    #
    #         last_line_json = json.loads(last_line)
    #
    #         print(last_line_json)
    #         l = last_line_json["data"]["card_number"]
    #
    #
    #
    #     except :
    #         time.sleep(0.5)

