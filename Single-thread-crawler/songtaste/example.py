#---------------------------------import---------------------------------------
import urllib2;

#------------------------------------------------------------------------------
def main():
    userMainUrl = "http://www.songtaste.com/user/351979/";
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    print "respHtml=",respHtml; # you should see the ouput html

###############################################################################
if __name__=="__main__":
    main();