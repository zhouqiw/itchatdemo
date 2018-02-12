# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: classer.py
@time: 2017/10/14 下午6:39
"""
from pchong.pchong_0 import *
import cv2
import PIL
import pylab
import numpy
from PIL import Image
import time

from datetime import datetime
from matplotlib import pyplot as plt
import requests
import os
import re
from sklearn.preprocessing import StandardScaler

import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

SessionId = ''
url_0 = 'http://www.shenzhentong.com/ajax/WaterMark.ashx'
url_1 = 'http://www.shenzhentong.com/service/invoice_101007009.html'
yzm = ''
'''
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36

'Cookie' :'ASP.NET_SessionId=t5y0212epxb5ztcv4r4zy0aq',
'''

hearders = {

'Referer':'http://www.shenzhentong.com/service/invoice_101007009.html',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}



payload = {
'tp':'1',
'yzm':'18',
'cardnum':'686049889',
}

hearders0 = {

'Referer':'http://www.shenzhentong.com/service/invoice_101007009.html',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}



payload0 = {
'tp':'3',
'jlsh':'',
'jzdh':'',
'jkh':'',
'jrq':'',
'jsj':'',
'jfirmfpmc':'上海弈力信息科技有限公司',
'jfirmsbh':'913102300938806162',
'jfirmaddre':'上海市崇明县竖新镇响椿路58号东三楼509室（上海竖新新经济开发区）',
'jfirmtel':'02154278708',
'jfirmyh':'中国银行漕河泾开发区支行',
'jfirmyhzh':'449466219808',
'jfirmphone':'18503052979'
}






def papiao(k,date_s):

    p_pay = []


    print "日期：", date_s

    rs = requests.session()
    res0 = rs.get(url_1)
    # print res0.text

    for img in os.listdir("img"):

        os.remove("img/" + img)

    with open('img1/kaptcha.jpg', 'wb') as f:
        res = rs.get(url_0)
        f.write(res.content)

    pil_image = PIL.Image.open('img1/kaptcha.jpg').convert('RGB')
    open_cv_image = numpy.array(pil_image)
    os.remove('img1/kaptcha.jpg')

    #打印图像
    plt.imshow(open_cv_image)
    pylab.show()

    imgray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # hierarchy


    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key=lambda x:x[1])
    ary1 = []
    for (c,_) in cnts:
        (x,y,w,h) = cv2.boundingRect(c)
        # print((x,y,w,h))
        if w >= 3 and h == 16 or h ==8  :
            ary1.append((x,y,w,h) )


    # ary =[(2, 5, 13, 16),(16,7,11,12),(28, 5, 12, 16),(43,7,11,12),(54,5,13,16)]
    #没有取加号
    ary = [(2, 5, 13, 16),  (28, 5, 13, 16),  (54, 5, 13, 16)]

    #
    # plt.imshow(open_cv_image)

    fig = plt.figure()
    for id, (x,y,w,h) in enumerate(ary):
        roi = open_cv_image[y:y+h, x:x+w]
        thresh = roi.copy()
        a = fig.add_subplot(1, len(ary), id+1)
        plt.imshow(thresh)

    ct = int(time.mktime(datetime.now().timetuple()))
    for id, (x,y,w,h) in enumerate(ary):
        fig = plt.figure()
        roi = open_cv_image[y:y+h, x:x+w]
        thresh = roi.copy()
        plt.imshow(thresh)
        plt.savefig('img/{}_{}.jpg'.format(ct, id+1), dpi=100)

    fig = plt.figure(figsize = (20,20))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    # print 'ok'
    # for  img in os.listdir('biaoji/10/'):
    #     print img
    for  idx, img in enumerate(os.listdir('img')):
        # print idx ,img
        if img =='.DS_Store':
            continue
                # print img
        else:
            # print idx ,img
            pil_image = PIL.Image.open('img/{}'.format(img)).convert('1')
            ax = fig.add_subplot(10, 12, idx+1, xticks=[], yticks=[])
            ax.imshow(pil_image,cmap=plt.cm.binary,interpolation='nearest')

    data = []
    basewidth = 50
    fig = plt.figure(figsize = (20,20))
    cnt = 0
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    for idx, img in enumerate(os.listdir('img/')):
        if img =='.DS_Store':

                # print img
            continue
        else:
            pil_image = PIL.Image.open('img/{}'.format(img)).convert('1')

            wpercent = (basewidth/float(pil_image.size[0]))
            hsize = int((float(pil_image.size[1])*float(wpercent)))
            img = pil_image.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            data.append([pixel for pixel in iter(img.getdata())])


    scaler = StandardScaler()
    scaler.fit(data)
    data_scaled = scaler.transform(data)

    from sklearn.externals import joblib
    clf = joblib.load('captcha.pkl')
    l= clf.predict(data_scaled)

    print l
    yzm =  int(l[0])+int(l[1])+int(l[2])
    print yzm

    time.sleep(2)

    payload['yzm'] = ''.join([str(yzm)])
    payload['cardnum'] = ''.join([str(k)])

    print payload


    res3 = rs.post('http://www.shenzhentong.com/Ajax/ElectronicInvoiceAjax.aspx', data = payload, headers = hearders)
    # print res3
    # res3.encoding = 'cp950'
    isok = str(res3.text)

    print isok
    if isok =='{"state":"100"}':
        print 'ok'
        url_2 = 'http://www.shenzhentong.com/service/fplist_101007009_686050919_20170930.html'.replace('686050919',str(k))\
                                                                                              .replace('20170930',str(date_s))

        print url_2

        res4 = rs.get(url_2)



        from lxml import etree

        page = etree.HTML(res4.text)


        print '*' * 20 + ' 获取表单数据' + '*' * 20

        hs = page.xpath('//tr[@class="odd_body"]')
        for h in hs:
            p_pay = h.values()

        hs1 = page.xpath('//td[@class="tdtjamt"]')
        for k in hs1:
            print k.values()[1]

        print p_pay
        if p_pay !=[]:

            payload0['jlsh'] = ''.join(p_pay[1])
            payload0['jzdh'] = ''.join(p_pay[2])
            payload0['jkh'] = ''.join(p_pay[3])
            payload0['jrq'] = ''.join(p_pay[4])
            payload0['jsj'] = ''.join(p_pay[5])
            # payload0['jsj'] =''.replace()
            hearders0['Referer'] =''.join(url_2)
            print payload0
            print hearders0
            res4 = rs.post('http://www.shenzhentong.com/Ajax/ElectronicInvoiceAjax.aspx', data=payload0,
                           headers=hearders0)

            print res4.headers
            print '*' * 20 + ' 提取开票标志' + '*' * 20
            print res4.content
            if res4.json()['state']=="1":
                return res4.json()['strs']

            # if res4["state"]=='1':
            #
            #     usl_1 = 'http://www.shenzhentong.com/service/fpdetail.aspx?nodecode=101007009&pid=9161772217981274983'.replace(res4['strs'])
            #     print usl_1



            # isok0 = str(res4.text)
            # # # print isok0['state']
            # print isok0
            # res4.encoding = 'cp950'
            # isok0 = str(res4.text)


            # print isok0

        print '*' * 20 + ' 获取表单数据' + '*' * 20








        # res3 = rs.post('http://www.shenzhentong.com/Ajax/ElectronicInvoiceAjax.aspx', data=payload, headers=hearders)

        # print '*' * 20 + '' + '*' * 20


    return 0