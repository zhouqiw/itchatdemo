# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: dl_img.py
@time: 2017/10/12 上午9:05
"""


import requests
# for i in xrange(100):
#     with open('img/kaptcha_{}.jpg'.format(i), 'wb') as f:
#         res = requests.get('http://www.shenzhentong.com/ajax/WaterMark.ashx')
#         f.write(res.content)
# from matplotlib import pylab
import cv2
import PIL
import pylab
import numpy
from PIL import Image
from matplotlib import pyplot as plt
# image = Image.open('kaptcha_0.img')

pil_image = PIL.Image.open('img/kaptcha_1.jpg').convert('RGB')
open_cv_image = numpy.array(pil_image)

# print open_cv_image
#
#
# plt.imshow(open_cv_image)
# pylab.show()

imgray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key=lambda x:x[1])

ary = []
print cnts
for (c,_) in cnts:
    (x,y,w,h) = cv2.boundingRect(c)
    print((x,y,w,h))
    if w >= 8 and h == 9   :
        ary.append((x,y,w,h) )


print(ary)

# plt.imshow(open_cv_image)
#
# pylab.show()

# from matplotlib import pyplot as plt
# fig = plt.figure()
# for id, (x,y,w,h) in enumerate(ary):
#     roi = open_cv_image[y:y+h, x:x+w]
#     thresh = roi.copy()
#     a = fig.add_subplot(1, len(ary), id+1)
#     plt.imshow(thresh)

# pylab.show()

# from matplotlib import pyplot as plt
# from datetime import datetime
# ct = int(time.mktime(datetime.now().timetuple()))
# for id, (x,y,w,h) in enumerate(ary):
#     fig = plt.figure()
#     roi = open_cv_image[y:y+h, x:x+w]
#     thresh = roi.copy()
#     plt.imshow(thresh)
#     plt.savefig('{}_{}.jpg'.format(ct, id+1), dpi=100)

# print(ary)