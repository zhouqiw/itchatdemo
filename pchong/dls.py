# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: dls.py
@time: 2017/10/14 下午7:20
"""

import requests
import re

for i in xrange(3):
    with open('img/kaptcha_{}.jpg'.format(i), 'wb') as f:
        res = requests.get('http://www.shenzhentong.com/ajax/WaterMark.ashx')
        f.write(res.content)
        decodedUnicodeStr = str(res.cookies)

        m_tr = decodedUnicodeStr.replace('<RequestsCookieJar[<Cookie ASP.NET_SessionId=','')\
                                .replace(' for www.shenzhentong.com/>]>','')
        print m_tr



        # date_arry = numpy.array(data)
        # date_arry.shape