
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
import urllib2
import re
import sys
import time
import re_test




def checkcard(i):

    reload(sys)
    sys.setdefaultencoding('utf8')
    # i = 686047550
    # i =686052158
    mys = re_test.mysql_dbs('agent')

    value = {}
    # i= i+1
    value['cardno'] = str(i)

    data = urllib.urlencode(value)
    # print type(data)
    url = 'http://query.shenzhentong.com:8080/sztnet/qryCard.do'

    req = urllib2.Request(url, data)
    res = urllib2.urlopen(req).read()


    # 假设当前respHtml是GBK编码类型的
    htmlCharset = "GBK";
    decodedUnicodeStr = res.decode(htmlCharset);
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
        if str(tuples[1]) > '2017-10-28 19:10:14':
            print tuples[1]
            print '*'*25
            mys.insert(tuples)
            print tuples
            if float(tuples[2]) > 84:
                print '***************  get a arriluble car  **************'
                mys.insert_0(tuples)
                print tuples

        time.sleep(2)
        return 1,tuples





    except IndexError, e:
        print e
        print ("i=",i)
        time.sleep(2)
        return 0,()





