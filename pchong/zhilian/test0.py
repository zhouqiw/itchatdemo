# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test0.py
@time: 2018/1/15 下午11:07
"""


import urllib
import urllib2
import re
import sys
import time






reload(sys)
sys.setdefaultencoding('utf8')
# i = 686047550
# i =686052158

# print type(data)
url = 'http://query.shenzhentong.com:8080/sztnet/qryCard.do'

req = urllib2.Request(url, data)
res = urllib2.urlopen(req).read()


# 假设当前respHtml是GBK编码类型的
htmlCharset = "GBK";
decodedUnicodeStr = res.decode(htmlCharset);