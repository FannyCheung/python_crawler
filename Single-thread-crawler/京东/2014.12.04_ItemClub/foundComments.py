#---------------------------------import---------------------------------------
#coding=utf-8
import urllib2,sys;
from bs4 import BeautifulSoup

#------------------------------------------------------------------------------
def main():
	url = "http://club.jd.com/review/1166360455-3-1-0.html"
	resp = urllib2.urlopen(url) #打开连接
	respHtml = resp.read() #获取页面内容
	soup=BeautifulSoup(respHtml,from_encoding="gb18030")
#	print (soup.title).encode('gb18030')  ##屏幕输出，没乱码
	a = str(soup.find_all('dl'))

	##获取内容写入txt
	file = open("d:\\python2.7.8\\data\\00000.txt","w")
	file.write(a)
	file.close()

	
	#print(soup.prettify())

	#	foundComments = re.findall('得：</dt>\n\n(?P<comments>.+?)</dd>',respHtml);	
#	respHtml1 = respHtml.decode('utf-8')
	
#	if re.match(ur'得：</dt>.+("[\u4e00-\u9fa5].+?)</dd>',respHtml,re.S):

	
#	fp = open("d:\\python2.7.8\\data\\comments_JD.txt","w")   # 打开文本
#	fp.write('\n'.join(foundComments))    # 写入数据
#	fp.close()   # 关闭文件

#### 匹配中文字
#	ss = s.decode('utf-8')     
#	re_words = re.compile(u"[\u4e00-\u9fa5]+")
##	m = re_words.search(ss,0)
#	print m.group()

	
###############################################################################
if __name__=="__main__":
    main();