#---------------------------------import---------------------------------------
#coding=utf-8
import urllib2,re,sys; 
 
#------------------------------------------------------------------------------
def main():
	userMainUrl = "http://list.jd.com/list.html?cat=9847%2C9848%2C11972&ev=&page=1&sort=sort_commentcount_desc&JL=4_5_0";
	req = urllib2.Request(userMainUrl);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	foundItemID = re.findall('name="(?P<ItemID>.+?)"\s+?class', respHtml);
#	print foundItemID[0];	

	fp = open("d:\\python2.7.8\\data\\list_itemClub_Herf_JD.txt","a");  # 商品评论页面club 连接list  保存
	
	i=0;
	h1='http://club.jd.com/review/';    ###http://club.jd.com/review/ 996967 -3-1-0.html
	h2='-3-1-0.html';
	for listclub in foundItemID:
		listclub = h1+foundItemID[i]+h2;
		i+=1;
		fp.write(listclub+"\n")    #写入数据，列表转字符串，用'\n'换行分隔
	fp.close()     #关闭文件	
	
	listID='\n'.join(foundItemID);  #商品ID连接成一个list
	fp = open("d:\\python2.7.8\\data\\list_itemID_JD_new.txt","w");   # 商品ID list 保存
	fp.write(listID)    #写入数据，列表转字符串，用'\n'换行分隔
	fp.close()     #关闭文件 
	

	




###############################################################################
if __name__=="__main__":
    main();