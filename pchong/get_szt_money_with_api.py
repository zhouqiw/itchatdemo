# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: get_szt_money_with_api.py
@time: 2018/12/26 下午11:13
"""
import requests
import sys
import json
import time
import random
import re_test

reload(sys)
sys.setdefaultencoding('utf8')
s = ''
with open("ip_pool",'r') as f :
    s = f.read()

list = s.split(',')

def getinfo(id):
    proxy_host = "https://" + list[random.randint(0, 50)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'https': proxy_host
    }
    url = 'https://api.apijs.cn/shenzhentong/'
    # id = '686047550'
    print url + str(id)
    result =  requests.get(url+str(id),headers = headers).text
    rs = json.loads(result)
    # print rs
    # print rs["code"]
    if rs["code"] == 0:
        return rs["data"]["card_number"],rs["data"]["balance_time"],rs["data"]["card_balance"]
        # print  rs["data"]["card_number"],rs["data"]["balance_time"],rs["data"]["card_balance"]
        return result
    else:
        print 'not found !'
        return result

if __name__ == '__main__':
    mys = re_test.mysql_dbs('agent')
    l = mys.get_id()[-1:][0][0] + 1
    i = 0
    #
    # s = time.time()
    # with open('2.txt','a+') as f :
    #     while i < 100:
    #         f.write(getinfo(l+i)+'\n')
    #         i= i + 1
    #
    # print time.time()-s

    s = time.time()
    while i < 800:
        a, b ,c = getinfo(l+i)
        mys.insert_1(a,b,c.replace('元',''))
        i = i + 1
    print time.time()-s