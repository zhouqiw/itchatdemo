# encoding: utf-8
# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: getyzm.py
@time: 2018/1/22 下午12:20
"""

import requests
import os
import cv2
import pylab
from matplotlib import pyplot as plt
import PIL
import numpy


import sys
reload(sys)
sys.setdefaultencoding('utf8')
# for i in xrange(100):
#     with open('kaptcha_{}.jpg'.format(i), 'wb') as f:
#         res = requests.get('https://my.zhaopin.com/myzhaopin/picturetimestamp.asp?t=1516594670045')
#         f.write(res.content)




url = 'https://my.zhaopin.com/myzhaopin/picturetimestamp.asp?t=1516594670045'


def getfiles(url,filename):
    with open(filename, 'wb') as f:
        res = requests.get(url)
        f.write(res.content)


def makedir(path):

    path = path.strip()

    path = path.rstrip("/")

    isExists = os.path.exists(path)


    if not isExists:

        os.makedirs(path)

        print path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + ' 目录已存在'
        return False

        # 定义要创建的目录

#

# for i in xrange(10):
#     value = raw_input('input a string:')
#     mkpath = "imgs/web".replace("web",str(value))
#     makedir(mkpath)
#     print value
#     filename = 'imgs/{}/{}_{}.jpg'.format(value,value,i)
#     getfiles(url,filename)



for  idx, img in enumerate(os.listdir('img')):
    # print idx ,img
    if img =='.DS_Store':
        continue

    else:

        pil_image = PIL.Image.open('img/{}'.format(img)).convert('RGB')
        open_cv_image = numpy.array(pil_image)

        plt.imshow(open_cv_image)
        pylab.show()

        # imgray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        # ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        # image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # # hierarchy
        #
        #
        # cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key=lambda x: x[1])
        # ary1 = []
        # for (c, _) in cnts:
        #     (x, y, w, h) = cv2.boundingRect(c)
        #     # print((x,y,w,h))
        #     if w >= 3 and h == 16 or h == 8:
        #         ary1.append((x, y, w, h))
        #
        # # ary =[(2, 5, 13, 16),(16,7,11,12),(28, 5, 12, 16),(43,7,11,12),(54,5,13,16)]
        # # 没有取加号
        # ary = [(2, 5, 13, 16), (28, 5, 13, 16), (54, 5, 13, 16)]
        #
        # #
        # # plt.imshow(open_cv_image)
        #
        # fig = plt.figure()
        # for id, (x, y, w, h) in enumerate(ary):
        #     roi = open_cv_image[y:y + h, x:x + w]
        #     thresh = roi.copy()
        #     a = fig.add_subplot(1, len(ary), id + 1)
        #     plt.imshow(thresh)
        #
        # fig = plt.figure(figsize=(20, 20))
        # fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
        #
        #



"""

获取控制台输入
value = input('input a int:')
print value
hello = raw_input('input a string:')
print hello

"""


