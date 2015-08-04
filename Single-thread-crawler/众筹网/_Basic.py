# -*- coding: utf-8 -*-  
import urllib2,urllib,re,sys,requests

#项目汇总页面
#for page in range(1,5):

#	url = "http://www.zhongchou.com/browse/id-10000-p-" + str(page)
#	page += 1
#	req = requests.get(url)
#	html = req.text

url = "http://www.zhongchou.com/browse/id-10000-p-3"
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
req = urllib2.Request(url, headers = headers)
html = urllib2.urlopen(req).read()	
	
#req = requests.get(url)
#html = req.text
	
#项目id
item_id = re.findall('href="/deal-show/id-(.*?)".*?ItemTextLink">',html,re.S)
file = open("d:\\PYTHONexercise\\data\\node_id\\page3_item_id.txt","a")
file.write('\n'.join(item_id))
file.write('\n')
file.close()

file = open("d:\\PYTHONexercise\\data\\node_id\\page3_dealer-id.txt","a")
i = 0
for url_item_id in item_id:   
	url_item_id = "http://www.zhongchou.com/deal-dealitem/id-" + item_id[i]   #交易页面
	i += 1
	req_item = requests.get(url_item_id)
	html_item = req_item.text

	#交易者id
	dealer_id = re.findall('<tr><td.*?/id-(.*?)">',html_item,re.S)
	file.write('\n'.join(dealer_id))
	file.write('\n#############\n')
file.close()
	
	
	
		
#		file = open("d:\\PYTHONexercise\\data\\node_id\\dealer_id.txt","a")
#		file.write('\n'.join(dealer_id))
#		file.write('\n')
#		file.close()






#url = "http://www.zhongchou.com/deal-topic/id-122800"
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#headers = {'User-Agent' : user_agent}
#req = urllib2.Request(url, headers = headers)
#html = urllib2.urlopen(req).read()

#comment_page_href = re.findall('下一页.*?-p-(.*?)\'.*?</a>',html,re.S)
#print comment_page_href

#file = open("d:/PYTHONexercise/data/test.txt","w")
#file.write('\n'.join(comment_page_href))
#file.close()	



		





