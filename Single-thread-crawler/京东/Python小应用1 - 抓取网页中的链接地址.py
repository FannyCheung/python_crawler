import html.parser as parser
import urllib.request

class MyHtmlParser(parser.HTMLParser):
    def __init__(self, lst = None):
 #       super().__init__()   #这里容易漏掉导致出错
        if not lst:
            self.urls = []
        else:
            self.urls = lst
        
    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if "http" in value and ".js" not in value \
            and value not in self.urls:
                self.urls.append(value)
                
    def handle_startendtag(self, tag, attrs):
        for attr, value in attrs:
            if "http" in value and ".js" not in value \
            and value not in self.urls:
                self.urls.append(value)


def ParseUrlsInText(text, lst):
    pars = MyHtmlParser(lst)
    try:
        pars.feed(text)
    #添加异常处理，可能会遇到各种异常
    except parser.HTMLParseError as ex:
        print("parse failed.",ex)
		
def VisitUrlsInPage(pageUrl):
    url_list = [pageUrl]
    for url in url_list:
        try:
            fh = urllib.request.urlopen(url)
            data = fh.read()
            ParseUrlsInText(str(data), url_list)
            #这里是为了快速结束，去掉就变成小爬虫了
            if len(url_list) >= 200: 
                break
        except urllib.request.URLError:
            print("Failed.")
            continue
    print("length: ", len(url_list))
    for url in url_list:
        print(url)


if __name__ == '__main__':
    VisitUrlsInPage("http://www.cnblogs.com/jason-yang/")