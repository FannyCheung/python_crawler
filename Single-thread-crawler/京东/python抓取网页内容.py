#coding=utf-8

import sys, urllib2

def main():
	url ="http://club.jd.com/review/1166360455-3-1-0.html" #��ҳ��ַ
	wp = urllib2.urlopen(url) #������
	content = wp.read() #��ȡҳ������
	fp = open("d:\\python2.7.8\\data\\test.txt","w") #��һ���ı��ļ�
	fp.write(content) #д������
	fp.close() #�ر��ļ�
	
if __name__=="__main__":
	main();