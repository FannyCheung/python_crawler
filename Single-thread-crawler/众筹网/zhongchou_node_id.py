# -*- coding: utf-8 -*-  
import urllib2,urllib,re,sys,requests

#项目汇总页面
for page in range(1,2):

	url = "http://www.zhongchou.com/browse/id-10000-p-" + str(page)
	page += 1
#	user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
#	headers = {'User-Agent' : user_agent}
#	req = urllib2.Request(url, headers = headers)
#	html = urllib2.urlopen(req).read()

	req = requests.get(url)
	html = req.text
	
	item_id = re.findall('href="/deal-show/(.*?)".*?ItemTextLink">',html,re.S)
	
	#交易页面
	i = 0
	for url_item_id in item_id:   
		url_item_id = "http://www.zhongchou.com/deal-dealitem/" + item_id[i]   #交易页面
		i += 1
#		req_item = urllib2.Request(url_item_id,headers = headers)
#		html_item = urllib2.urlopen(req_item).read()

		req_item = requests.get(url_item_id)
		html_item = req_item.text
	
		#交易者id
		dealer_id = re.findall('<tr><td.*?/id-(.*?)">',html_item,re.S)
		file = open("d:/PYTHONexercise/data/node_id/test_dealer_id.txt","a")
		file.write('\n'.join(dealer_id))
		file.write('\n')
		file.close()	



