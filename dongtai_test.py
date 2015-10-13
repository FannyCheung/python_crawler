#coding:utf-8

import urllib2

url = "http://beian.hndrc.gov.cn/indexinvestment.jsp?id=162518"
html = urllib2.urlopen(url).read()
print html.decode('utf-8').encode('gb2312')