# encoding: utf-8

import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT)
def simple_reply(TEXT):
    print(msg.text)

itchat.auto_login(hotReload=True)
itchat.run()