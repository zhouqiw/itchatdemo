# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: couse_93.py
@time: 2017/10/15 上午11:11
"""

import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

import PIL
import numpy
import os


basewidth = 50
pil_image = PIL.Image.open('biaoji/8/1507978282_2.jpg').convert('1')
wpercent = (basewidth/float(pil_image.size[0]))
hsize = int((float(pil_image.size[1])*float(wpercent)))
img = pil_image.resize((basewidth,hsize), PIL.Image.ANTIALIAS)




digits = []
labels = []
basewidth = 50
fig = plt.figure(figsize=(20, 20))
cnt = 0
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(0, 10):
    for imgs in os.listdir('biaoji/{}/'.format(i)):

        if   imgs == '.DS_Store':

            os.remove('biaoji/{}/'.format(i) + imgs)

    for img in os.listdir('biaoji/{}/'.format(i)):
        #         if os.listdir('biaoji/{}/'.format(i))[:1][0]=='.DS_Store':
        #             break


        pil_image = PIL.Image.open('biaoji/{}/{}'.format(i, img)).convert('1')

        wpercent = (basewidth / float(pil_image.size[0]))
        hsize = int((float(pil_image.size[1]) * float(wpercent)))
        img = pil_image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

        ax = fig.add_subplot(10, 200, cnt + 1, xticks=[], yticks=[])
        ax.imshow(img, cmap=plt.cm.binary, interpolation='nearest')
        ax.text(0, 7, str(i), color="red", fontsize=20)
        cnt = cnt + 1

        digits.append([pixel for pixel in iter(img.getdata())])
        labels.append(i)


import numpy
digit_ary  = numpy.array(digits)

print digit_ary




from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(digit_ary)
X_scaled = scaler.transform(digit_ary)



mlp = MLPClassifier(hidden_layer_sizes=(30,30,30), activation='logistic', max_iter = 50000)
mlp.fit(X_scaled,labels)

from sklearn.externals import joblib
joblib.dump(mlp, 'captcha.pkl')
predicted = mlp.predict(X_scaled)


print predicted


target = numpy.array(labels)

print predicted == target


import os
import PIL

fig = plt.figure(figsize = (20,20))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
print 'ok'
# for  img in os.listdir('biaoji/10/'):
#     print img
for  idx, img in enumerate(os.listdir('biaoji/10')):
    print idx ,img
    if img =='.DS_Store':
            print img
    else:
        print idx ,img
        pil_image = PIL.Image.open('biaoji/10/{}'.format(img)).convert('1')
        ax = fig.add_subplot(10, 12, idx+1, xticks=[], yticks=[])
        ax.imshow(pil_image,cmap=plt.cm.binary,interpolation='nearest')








data = []
basewidth = 50
fig = plt.figure(figsize = (20,20))
cnt = 0
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for idx, img in enumerate(os.listdir('img/')):
    if img =='.DS_Store':
            print img
    else:
        pil_image = PIL.Image.open('img/{}'.format(img)).convert('1')

        wpercent = (basewidth/float(pil_image.size[0]))
        hsize = int((float(pil_image.size[1])*float(wpercent)))
        img = pil_image.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
        data.append([pixel for pixel in iter(img.getdata())])









scaler = StandardScaler()
scaler.fit(data)
data_scaled = scaler.transform(data)



print mlp.predict(data_scaled)