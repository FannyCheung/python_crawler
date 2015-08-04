#coding=utf-8

import sys, urllib2

def main():
	url ="http://club.jd.com/review/1166360455-3-1-0.html" #网页地址
	wp = urllib2.urlopen(url) #打开连接
	content = wp.read() #获取页面内容
	fp = open("d:\\python2.7.8\\data\\test.txt","w") #打开一个文本文件
	fp.write(content) #写入数据
	fp.close() #关闭文件
	
if __name__=="__main__":
	main();