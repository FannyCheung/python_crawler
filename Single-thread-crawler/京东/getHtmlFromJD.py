#------------import------------------
import urllib2;

#------------------------------------
def main():
	userMainUrl = "http://club.jd.com/review/996967-3-1-0.html";
	req = urllib2.Request(userMainUrl);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	print "respHtml=",respHtml;
	
#####################################################
if __name__=="__main__":
	main();