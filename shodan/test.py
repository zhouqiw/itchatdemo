# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test.py
@time: 2019/1/12 下午8:39
"""

import shodan

SHODAN_API_KEY = "insert your API key here"

api = shodan.Shodan('JbpGdKrAFAgpVPEBN9LXmS0UCJ5dWSkz')


try:
    # Search Shodan
    results = api.search('mongodb')

    # Show the results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')
except shodan.APIError, e:
    print('Error: {}'.format(e))