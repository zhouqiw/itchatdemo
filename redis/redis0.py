# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: redis0.py
@time: 2017/12/1 下午10:30
"""

import redis


pool = redis.ConnectionPool(host ='127.0.0.1',port=6379)
r = redis.Redis(connection_pool = pool)
# print conn.flushdb()
p = r.pipeline()
p.set('hello','redis')
p.sadd('faz','baz')
p.incr('num')
print p.execute()
print r.get('hello')


# r.hset('users:jdoe',  'name', "John Doe")
# r.hset('users:jdoe', 'email', 'John@test.com')
# r.hset('users:jdoe', 'phone', '1555313940')
# r.hincrby('users:jdoe', 'visits', 1)
print r.hgetall('users:jdoe')
print r.hkeys('users:jdoe')
print r.hvals('users:jdoe')