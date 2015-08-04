#-------------------import-   use re to fetch HREF-------------------
import urllib2;
import re;

#----------------------------------------------
def main():
	userMainUrl = "http://club.jd.com/review/996967-3-1-0.html";
	req = urllib2.Request(userMainUrl);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	print "respHtml=",respHtml;
	#<a href="Href" target="_blank"
	foundHref = re.search('<dt>"(?P<href>.+?)"\s+?target</dd>',respHtml);
	print"foundHref=",foundHref;
	if(foundHref):
		Href = foundHref.group("href");
		print "Href=", Href ;
	
###################################################
if __name__=="__main__":
	main();