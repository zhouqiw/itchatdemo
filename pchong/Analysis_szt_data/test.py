# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test.py
@time: 2018/12/27 下午9:28
"""

import sys
sys.path.append('../')
import get_szt_money_with_api_0 as gapi

import sqlalchemy as al
print al.__version__


# !/usr/bin/python

from sqlalchemy import create_engine, text, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'card'
    # Sequence('id'), primary_key = True

    id = Column(Integer,Sequence('id'), primary_key = True)
    time = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return "<Product(id={0}, time={1}, price={2})>".format(self.id, self.time, self.price)


class ok(Base):
    __tablename__ = 'ok_card'
    # Sequence('id'), primary_key = True

    id = Column(Integer,Sequence('id'), primary_key = True)
    ctime = Column(String)
    monny = Column(Integer)

    def __repr__(self):
        return "<Product(id={0}, time={1}, price={2})>".format(self.id, self.ctime, self.monny)


class analysis(Base):
    __tablename__ = 'analysis'
    # Sequence('id'), primary_key = True

    id = Column(Integer,Sequence('id'), primary_key = True)
    first_time = Column(String)
    remainder_0 = Column(Integer)
    second_time = Column(String)
    remainder_1 = Column(Integer)

    def __repr__(self):
        return "<Product(id={0}, fist_time={1}, remainder_0={2}, second_time={3}, remainder_0={4})>".format(self.id, self.first_time,self.remainder_0, self.second_time,self.remainder_1)

# class pidok(Base):
#     __tablename__ = 'pid'
#     # Sequence('id'), primary_key = True
#
#     numr = Column(Integer,Sequence('numr'), primary_key = True)
#     id  = Column(Integer)
#     pid = Column(Integer)
#
#     def __repr__(self):
#         return "<pidok(numr='%d', id='%d', pid='%d')>" % (self.numr, self.id, self.pid)


DB_CON_STR = 'mysql+mysqldb://root:rooter@localhost/agent?charset=utf8'
engine = create_engine(DB_CON_STR, echo=False)  # True will turn on the logging

Session = sessionmaker(bind=engine)
session = Session()

# eg1 via class
res = session.query(analysis).all()
print res
# res = session.query(Product).filter(text("id=686050815")).one()

#
# a,b,c = gapi.getinfo(666672303)
# print a,b,c

# res = session.query(Product).filter(Product.price < 10).filter(Product.time > '2018-12-25 08:19:51' ).order_by(Product.price)
res = session.query(Product).filter(Product.price > 100).filter(Product.time > '2018-12-20 08:19:51' )
n = 0
for i in res:
    print i.id,i.time,i.price
    a,b,c = gapi.getinfo(i.id)
    print a,b,c

    new_obj = analysis(id=i.id, first_time=i.time,remainder_0=i.price,second_time=b,remainder_1=c)
    session.add(new_obj)
    session.commit()
    print "*"*30
    n = n+1



print '10元以下：{}'.format(n)
#
# res = session.query(Product).filter(Product.price > 10).filter(Product.price < 40).filter(Product.time > '2018-12-25 08:19:51' ).order_by(Product.price)
# n = 0
# for i in res:
#     n = n+1
# print '10元以上40以下：{}'.format(n)
#
# res = session.query(Product).filter(Product.price > 40).filter(Product.price < 60).filter(Product.time > '2018-12-25 08:19:51' ).order_by(Product.price)
# n = 0
# for i in res:
#     n = n+1
# print '40元以上60以下：{}'.format(n)
#
#
# res = session.query(Product).filter(Product.price > 80).filter(Product.price < 100).filter(Product.time > '2018-12-25 08:19:51' ).order_by(Product.price)
# n = 0
# for i in res:
#     n = n+1
# print '80元以上100以下：{}'.format(n)
#
#
# res = session.query(Product).filter(Product.price > 100).filter(Product.time > '2018-12-25 08:19:51' ).order_by(Product.price)
# n = 0
# for i in res:
#     # print i.id,i.time,i.price
#     n = n+1
# print '100元以上：{}'.format(n)
#
# res = session.query(Product).filter(Product.time > '2018-12-25 08:19:51' ).order_by(Product.price)
# n = 0
# for i in res:
#     # print i.id,i.time,i.price
#     n = n+1
# print '总数是：{}'.format(n)


if __name__ == '__main__':
    pass