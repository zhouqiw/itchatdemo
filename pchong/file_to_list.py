# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: file_to_list.py
@time: 2018/12/26 下午9:13
"""
from bs4 import BeautifulSoup
import urllib



with open("1.txt") as f:
    soup = BeautifulSoup(f, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    #检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
          proxy_host = "https://" + ip
          proxy_temp = {"https": proxy_host}
          res = urllib.urlopen(url, proxies=proxy_temp).read()
        except Exception as e:
          ip_list.remove(ip)
          continue
    print ip_list
    with open("ip_pool",'w') as t:
        for i in ip_list:
            t.writelines(str(i)+',')
            t