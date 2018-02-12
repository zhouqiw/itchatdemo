# encoding: utf-8

import itchat

itchat.auto_login()

chatroomUserName = '@1234567'
friend = itchat.get_friends()[1]

r = itchat.add_member_into_chatroom(chatroomUserName, [friend])
# if r['BaseResponse']['ErrMsg'] == '':
#     status = r['MemberList'][0]['MemberStatus']
#     itchat.delete_member_from_chatroom(chatroom['UserName'], [friend])
#     return { 3: 'you friend put you blacklist', 4: 'you friend has delet you' , }.get(status,'you are friendship')

