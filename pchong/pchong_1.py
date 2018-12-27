
# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: pchong_0.py
@time: 2017/10/10 下午4:03
"""

# import urllib2
#
# response = urllib2.Request("http://query.shenzhentong.com:8080/sztnet/qryCard.do")
# print urllib2.urlopen(response)
# s ='你好'
# print s

import urllib
from urllib2 import Request,urlopen
import re
import sys
import time
import random

s = ''
with open("ip_pool",'r') as f :
    s = f.read()

list = s.split(',')
# print list
# print len(list)
#
# for i in xrange(1000):
#     j = random.randint(0,50)
#     # print list[j] , j
#     if j == 51:
#         print j
#
#     if j == 0:
#         print j





def checkcard(i):

    reload(sys)
    sys.setdefaultencoding('utf8')

    value = {}
    # i= i+1
    value['cardno'] = str(i)

    data = urllib.urlencode(value)
    # print type(data)
    url = 'http://query.shenzhentong.com:8080/sztnet/qryCard.do'
    # ip = "119.101.116.167:9999"
    proxy_host = "https://" + list[random.randint(0,50)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'https'     :  proxy_host
    }
    req = Request(url, data,headers=headers)
    res = urlopen(req).read()

    # 假设当前respHtml是GBK编码类型的
    htmlCharset = "GBK"
    decodedUnicodeStr = res.decode(htmlCharset)
    # print decodedUnicodeStr

    # from lxml import etree
    #
    # page = etree.HTML(res4.text)
    # hs = page.xpath('//tr[@class="odd_body"]')
    # for h in hs:
    #     print h.values()


    res_tr = r'<tr>(.*?)</tr>'

    m_tr =  re.findall(res_tr,decodedUnicodeStr,re.S|re.M)
    try:
        # print m_tr

        text=m_tr[0].replace("<td bgcolor='#E4F2F3'>卡号：</td><td bgcolor='#FFFFFF'>","")\
            .replace("</td><td bgcolor='#E4F2F3' id='cardRealAmt' width=10% nowrap>卡内余额(截止到","/")\
            .replace(")：</td><td bgcolor='#FFFFFF' align='right'>","/")\
            .replace("元</td><td bgcolor='#E4F2F3' id='expDate' width=10% nowrap>卡有效截止日期：</td><td bgcolor='#FFFFFF' align='right'>","/")\
            .replace("</td>","")
        inf = text.split('/')
        tuples = tuple(inf)
        print tuples
        if str(tuples[1]) > '2018-01-28 19:10:14':
            # print tuples[1]
            # print '*'*25
            #
            # print tuples
            # if float(tuples[2]) > 84:
            #     print '***************  get a arriluble car  **************'
            #     mys.insert_0(tuples)
            #     print tuples

            time.sleep(0.5)
            return 1,tuples

        else:
            return 0,()



    except IndexError, e:
        print e
        # print ("i=",i)
        time.sleep(20)
        return 0,()





