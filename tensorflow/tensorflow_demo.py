# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: tensorflow_demo.py
@time: 2017/10/25 下午4:05
"""

import tensorflow as tf

hello__op = tf.constant('hello, Tensorflows!')
a = tf.constant(10)
b = tf.constant(32)
compute = tf.add(a,b)


with tf.Session() as sess:
    print sess.run(hello__op)
    print sess.run(compute)