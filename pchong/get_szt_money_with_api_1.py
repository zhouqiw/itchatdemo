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
# import re_test

reload(sys)
sys.setdefaultencoding('utf8')
s = ''
with open("ip_pool",'r') as f :
    s = f.read()

list = s.split(',')
filename = '4.txt'

def getinfo(id):
    proxy_host = "https://" + list[random.randint(0, 50)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'https': proxy_host
    }
    url = 'https://api.apijs.cn/shenzhentong/'
    # id = '686047550'
    print url + str(id)
    result =  requests.get(url+str(id),headers = headers,timeout=1).text
    rs = json.loads(result)
    print rs
    # print rs["code"]
    if rs["code"] == 0:
        # return rs["data"]["card_number"],rs["data"]["balance_time"],rs["data"]["card_balance"]
        # print  rs["data"]["card_number"],rs["data"]["balance_time"],rs["data"]["card_balance"]
        return result
    else:
        print 'not found !'


        return None



def tast(l):

    i = 0



    s = time.time()

    with open(filename,'a+') as h :
        while i < 100:
            res = getinfo(l+i)
            if res != None:
                h.write(res+'\n')
            else:
                break
            i= i + 1

    print time.time()-s
    return i

    # s = time.time()
    # while i < 800:
    #     a, b ,c = getinfo(l+i)
    #     mys.insert_1(a,b,c.replace('元',''))
    #     i = i + 1
    # print time.time()-s


if __name__ == '__main__':
    r = 0

    while 1 :

        try:
            n = 0

            last_line = ''
            with open(filename, 'r') as f:  # 打开文件
                first_line = f.readline()  # 读第一行
                off = -50  # 设置偏移量
                while True:
                    f.seek(off, 2)  # seek(off, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
                    lines = f.readlines()  # 读取文件指针范围内所有行
                    if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
                        last_line = lines[-1]  # 取最后一行
                        break
                    # 如果off为50时得到的readlines只有一行内容，那么不能保证最后一行是完整的
                    # 所以off翻倍重新运行，直到readlines不止一行
                    off *= 2

                # print '文件' + fname + '第一行为：' + first_line
                # print '文件' + fname + '最后一行为：' + last_line

            last_line_json = json.loads(last_line)

            print(last_line_json)
            l = last_line_json["data"]["card_number"] + random.randint(2,20)+(100-n)
            # l = 666047550
            print(type(l))
            n = tast(l)
            print "*******"+ n


        except Exception as e:
            print e
            time.sleep(0.5)

        # time.sleep(5)
        # r = r+1
        # if r >100:
        #     break