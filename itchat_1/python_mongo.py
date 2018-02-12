# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: python_mongo.py
@time: 2017/12/13 上午11:03
"""

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)

db = conn.admin
my_set = db.test_set
# my_set.insert({"name":"zhangsan","age":18})
# users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20}]
# my_set.insert(users)

for i in my_set.find():
    print(i['age'])
    print(i['name'])