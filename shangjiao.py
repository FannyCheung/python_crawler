#coding:utf-8

import urllib2,re
from lxml import etree

start_url = "https://bbs.sjtu.edu.cn/bbstcon?board=PhD&reid=1406973178&file=M.1406973178.A&page=1"
response = urllib2.Request(start_url)
html_temp = urllib2.urlopen(response).read()
html = etree.HTML(html_temp)

user = html.xpath('//pre/text()[4]')
user1 = user[0].encode('gb2312')



#file = open('result_shangjiao.txt','w')
#file.write(str(user1)+'\n')
#file.close()
#
print user1

#print user

'//span[@class="floatR hui6 mt1"]/text()'