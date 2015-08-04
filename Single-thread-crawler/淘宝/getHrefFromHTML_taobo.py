#-------------------import-   use re to fetch HREF-------------------
import urllib2;
import re;

#----------------------------------------------
def main():
	userMainUrl = "http://item.taobao.com/item.htm?spm=a219r.lm5059.14.43.K97XVX&id=15157328298&ns=1&abbucket=1#detail";
	req = urllib2.Request(userMainUrl);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	print "respHtml=",respHtml;
	#<a href="Href" class
	foundHref = re.search('shortcut-label="(?P<href>.+?)"',respHtml);
	print"foundHref=",foundHref;
	if(foundHref):
		Href = foundHref.group("href");
		print "Href=", Href ;
	
###################################################
if __name__=="__main__":
	main();