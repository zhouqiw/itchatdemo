# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: db_sqlalchemy.py
@time: 2017/10/22 上午7:26
"""

# from flask_sqlalchemy import SQLAlchemy as al
# from sqlalchemy import ForeignKey

import sqlalchemy as al
print al.__version__
import classer

# !/usr/bin/python

from sqlalchemy import create_engine, text, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'card_0'
    # Sequence('id'), primary_key = True

    id = Column(Integer,Sequence('id'), primary_key = True)
    time = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return "<Product(id='%d', time='%s', price='%d')>" % (self.id, self.time, self.price)
#686064236



class pidok(Base):
    __tablename__ = 'pid'
    # Sequence('id'), primary_key = True

    numr = Column(Integer,Sequence('numr'), primary_key = True)
    id  = Column(Integer)
    pid = Column(Integer)

    def __repr__(self):
        return "<pidok(numr='%d', id='%d', pid='%d')>" % (self.numr, self.id, self.pid)


DB_CON_STR = 'mysql+mysqldb://root:rooter@localhost/agent?charset=utf8'
engine = create_engine(DB_CON_STR, echo=False)  # True will turn on the logging

Session = sessionmaker(bind=engine)
session = Session()

# eg1 via class
# res = session.query(Product).filter(Product.id==1).one()
# res = session.query(Product).filter(text("id=686050815")).one()


res = session.query(Product).all()

for i in res:


    print i.id, i.time[0:10].replace('-',''), i.price
    value_this =i.price
    date = int(i.time[0:10].replace('-',''))

    n = 10

    if value_this >160 and value_this <200:
        n = int((200-value_this)/5)
    elif value_this >80 and value_this <100:
        n = int((100-value_this)/5)

    else:
        n = 10

    while(n>0):

        p = classer.papiao(i.id,date)

        date = date - 1
        n = n -1
        if p == 0:
            print 'next'*20
            continue
        if p!= 0:

            new_obj = pidok(id = i.id, pid = p)
            session.add(new_obj)

            session.commit()
            break

# res = session.query(pidok).all()
#
# for i in res:
#     print i.id,i.pid

session.close()
