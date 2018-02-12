# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: wx_demo.py
@time: 2017/8/29 上午10:15
"""
from wxpy import *

bot = Bot(console_qr=True,cache_path=True)
# j = 0
# for i in bot.chats():
#     print i
#     j = j+1
#
# print j
friends = bot.friends()
# print friends.stats_text()
my_friend = bot.friends().search('心', sex=MALE, city="深圳")
print my_friend
# bot.file_helper.send('hello world')
#
# bot.self.send('hello world!')

