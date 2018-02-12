# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: urlencoded.py
@time: 2017/10/31 上午10:43
"""

import urllib
query_filter = {'song': '宽恕', 'artist': '王菲'}
query_parms = urllib.parse.urlencode(query_filter)
print query_parms
# 'artist=%E7%8E%8B%E8%8F%B2&song=%E5%AE%BD%E6%81%95'
query_url = 'http://www.example.com/query?{}'.format(query_parms)
print query_url
# 'http://www.example.com/query?artist=%E7%8E%8B%E8%8F%B2&song=%E5%AE%BD%E6%81%95'