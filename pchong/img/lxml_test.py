# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: lxml_test.py
@time: 2017/10/20 上午8:31
"""

import lxml.etree
import sys

html = ''''' 
<html> 
　　<head> 
　　　　<meta name="content-type" content="text/html; charset=utf-8" /> 
　　　　<title>友情链接查询 - 站长工具</title> 
　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc --> 
　　　　<meta name="Keywords" content="友情链接查询" /> 
　　　　<meta name="Description" content="友情链接查询" /> 

　　</head> 
　　<body> 
　　　　<h1 class="heading">Top News</h1> 
　　　　<p style="font-size: 200%">World News only on this page</p> 
　　　　Ah, and here's some more text, by the way. 
　　　　<p>... and this is a parsed fragment ...</p> 

　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a>  
　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a>  
　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a>  
　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a> 
　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a> 
　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a>  
　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a> 
       <div class="news"> 
        1. <b>无流量站点清理公告</b>  2013-02-22<br /> 
        取不到的内容11 
        </div> 
        <div class="news"> 
        2. <strong>无流量站点清理公告</strong>  2013-02-22<br />取不到的内容22 
        </div>  
        <div class="news"> 3. <span>无流量站点清理公告</span>  2013-02-22<br />取不到的内容33 
        </div>  
        <div class="news"> 4. <u>无流量站点清理公告</u>  2013-02-22<br />取不到的内容44 
        </div> 
        
        
                       <div class="query_result" style="display: block;">
                        <div class="topbar">查询结果</div>
                        <table class="listtable" style="">
                            <tr class="head">
                                <th></th>
                                <th>卡号</th>
                                
                                <th>充值时间</th>
                                <th>充值金额</th>
                                <th>发票状态</th>
                            </tr>

                            <tr class="odd_body" lsh="11" zdh="293000514" kh="686047628" rq="20171009" sj="183516"><td class="first_th"> <input class="ipcbcxjg" name="first_res" type="checkbox" value="11"></td><td>686047628</td><td>20171009</td><td class="tdtjamt" val="100">100元</td><td class="invoice_info"></td></tr>
                        </table>
                        
                        <div class="apply_btn" style=""><span style="cursor: pointer;">申请电子发票</span></div>
                    </div>
    　　</body> 
</html> 
'''

page = lxml.etree.HTML(html.decode(
    'utf-8'))  # 先确保html经过了utf-8解码，即code = html.decode('utf-8', 'ignore')，否则会出现解析出错情况。因为中文被编码成utf-8之后变成 '/u2541'　之类的形式，lxml一遇到　“/”就会认为其标签结束。
hrefs = page.xpath("//tr")  # 它会找到整个html代码里的所有a标签，如果想精确地获取，可以采用下面获取p标签的方法
for href in hrefs:
    print href.get('zdh')
    print href.get('kh')
    # print href.get('val')
    # print href.text.encode("utf-8")
    print '*' * 20 + '华丽的星号分界线' + '*' * 20


hs = page.xpath('//tr[@class="odd_body"]')
for h in hs:
    print(h.values())
    # print(h.text)
hs1 = page.xpath('//input[@class="ipcbcxjg"]')
for j in hs1:
    print j.values()

hs1 = page.xpath('//td[@class="tdtjamt"]')
for k in hs1:
    print k.values()

# ts = page.xpath('/html//*')
# for t in ts:
#     print(t.tag)
# ps = page.xpath("/html/body/p[@style='font-size: 200%']")  # 精确获取p标签，如果使用xpath('//p')将会找到整个html代码里的所有p标签
# # 等价ps = page.xpath("//p[@style='font-size: 200%']")#相对路径
# # 等价ps = page.xpath("//p[text()='World News only on this page']")#标签里面没有属性时，为了精确获取某个标签，可以使用text()，position()等方法来过滤
# for p in ps:
#     print p.values()
#     print p.text.encode('utf8')  # 获取p标签下的文本内容
#
# print '-' * 40 + "华丽的分界线" + '-' * 40
#
# hard_get = page.xpath("//br")
# for hg in hard_get:
#     print '---' + hg.tail.encode(
#         'utf8').strip() + '---'  # 使用lxml.etree._Element的tail属性来获取br标签后面紧跟的文本内容（仅仅使用xpath是很难获取这个内容的）
#
# print '-' * 40 + "华丽的分界线" + '-' * 40
#
# html1 = """
# <html><head><title>为什么len(y) <= 1</title><script>var y = 1</script></head>sample.<html>
# """
# # lxml.etree.HTML可以处理内容中含有特殊字符的情况，如上边title标签的文本内容中含有"<"。
# page1 = lxml.etree.HTML(html1.decode('utf8'))
# title = page1.xpath("//title")[0].text
# print 'title:%s' % title.encode('utf-8')
#
# print '-' * 40 + "华丽的分界线" + '-' * 40
#
# # bs4的BeautifulSoup解析器也可以处理内容中含有特殊字符的情况，如上边title标签的文本内容中含有"<"。
# from bs4 import BeautifulSoup
#
# root = BeautifulSoup(''.join(html1), 'lxml')
# print "Title is : " + root.head.title.string.encode('utf8')
#
# print '-' * 40 + "华丽的分界线" + '-' * 40
#
# from lxml.html import clean
#
# # 如果script与style标签之间的内容影响解析页面，或者页面很不规则，可以使用lxml.html.clean模块。模块 lxml.html.clean 提供 一个Cleaner 类来清理 HTML 页。它支持删除嵌入或脚本内容、 特殊标记、 CSS 样式注释或者更多。
# # 注意,page_structure,safe_attrs_only为False时保证页面的完整性，否则，这个Cleaner会把你的html结构与标签里的属性都给清理了。使用Cleaner类要十分小心，小心擦枪走火。
# cleaner = clean.Cleaner(style=True, scripts=True, page_structure=False, safe_attrs_only=False)
# print '原始字符串:\n%s' % html1.strip()
# print 'clean_up之后的字符串:\n%s' % cleaner.clean_html(html1.decode('utf8')).encode('utf8').strip()