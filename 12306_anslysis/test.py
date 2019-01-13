# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test.py
@time: 2019/1/3 下午1:40
"""
import sys
reload(sys)
sys.setdefaultencoding('gbk')
from sqlalchemy import create_engine, text, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class analysis_123(Base):
    __tablename__ = '12306_analysis'
    # Sequence('id'), primary_key = True

    mail_id  =  Column(String, primary_key = True)
    username =  Column(String)
    name     =  Column(String)
    sfz_id   =  Column(String)
    passwd   =  Column(String)
    iphone_id = Column(String)


    def __repr__(self):
        return "<Product(mail_id={0}, username={1}, name={2}, sfz_id={3}, passwd={4},iphone_id={5}>".format(self.mail_id, self.username,self.name, self.sfz_id,self.passwd,self.iphone_id)




DB_CON_STR = 'mysql+mysqldb://root:rooter@localhost/agent?charset=utf8'
engine = create_engine(DB_CON_STR, echo=False)  # True will turn on the logging

Session = sessionmaker(bind=engine)
session = Session()

res = session.query(analysis_123).all()
print res

with open('/Users/zhouqi/Downloads/info(1).txt','r') as f :
    print(f.readline().split('----')[2].encode('utf-8'))
    print(f.readline().encode('utf-8'))
    info = f.readlines()
    for i in info:
        l =  i.encode('utf-8').split('----')
        # print l[0],l[1],l[2],l[3],l[4],l[5]
        new_obj = analysis_123(mail_id=l[0], username=l[1], name=l[2], sfz_id=l[3], passwd=l[4],iphone_id=l[5])
        session.add(new_obj)
        session.commit()




