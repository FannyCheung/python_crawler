#---------------------------------import---------------------------------------
#coding=utf-8
import urllib2,sys,re;
from bs4 import BeautifulSoup

#------------------------------------------------------------------------------
def main():
	userMainUrl = "http://list.jd.com/list.html?cat=9847%2C9848%2C11972&ev=&page=1&sort=sort_commentcount_desc&JL=4_5_0";
	req = urllib2.Request(userMainUrl);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	foundItemID = re.findall('name="(?P<ItemID>.+?)"\s+?class', respHtml);
##	fp = open("d:\\python2.7.8\\data\\list_itemClub_Herf_JD.txt","a");  # 商品评论页面club 连接list  保存
	i=0;
	h1='http://club.jd.com/review/';    ###http://club.jd.com/review/ 996967 -3-1-0.html
	h2='-3-1-0.html';
	for listclub in foundItemID:
		listclub = h1+foundItemID[i]+h2;
		i+=1;
##		fp.write(listclub+"\n")    #写入数据，列表转字符串，用'\n'换行分隔
##		fp.close()     #关闭文件	
		req2=urllib2.Request(listclub);
		resp2=urllib2.urlopen(req2)
		respHtml2 = resp2.read()
		soup=BeautifulSoup(respHtml2,from_encoding="gb18030")
		a = str(soup.find_all('dl'))
		##获取内容写入txt
		file = open("d:\\python2.7.8\\data\\12.11\\roughdataZZZ.txt","a")
		file.write(a)
		file.close()
###############################################################################
if __name__=="__main__":
	main();