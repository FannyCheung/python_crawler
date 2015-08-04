#---------------------------------import---------------------------------------
#coding=utf-8
import urllib2,re,sys; 
 
#------------------------------------------------------------------------------
def main():
	userMainUrl = "http://list.jd.com/list.html?cat=9847%2C9848%2C11972&ev=&page=1&sort=sort_commentcount_desc&JL=4_5_0";
	req = urllib2.Request(userMainUrl);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	foundItemHerf = re.findall('p-name”><a\s+?target="_blank"\s+?herf="(?P<ItemID>.+?)"onclick', respHtml);
	fp = open("d:\\python2.7.8\\data\\list_itemHerf_JD.txt","w");
	fp.write(','.join(foundItemHerf)) #写入数据，列表转字符串，用','分隔
	fp.close() #关闭文件 

 
###############################################################################
if __name__=="__main__":
    main();