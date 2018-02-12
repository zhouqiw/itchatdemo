# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test.py
@time: 2017/10/15 下午1:44
"""


import cookielib, urllib2 , pprint

import lxml.html
import lxml.cssselect

def parse_form(html):
    tree = lxml.html.fromstring(html)
    # print tree
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data




# REGISTER_URL ='http://www.shenzhentong.com/service/invoice_101007009.html'
REGISTER_URL = 'http://www.shenzhentong.com/index.html'

cj = cookielib . CookieJar ( )
# opener = urllib2 . build_opener (urllib2 . HTTPCookieProcessor (cj))

html = urllib2.urlopen(REGISTER_URL).read()
form = parse_form(html)

pprint.pprint(form)