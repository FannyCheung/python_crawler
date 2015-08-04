# -*- coding: utf-8 -*-  
import urllib2,urllib,re,sys,time

#项目汇总页面
for page in range(1,5):
	url = "http://www.zhongchou.com/browse/id-10000-p-" + str(page)
	page += 1
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent' : user_agent}
	req = urllib2.Request(url, headers = headers)
	html = urllib2.urlopen(req).read()
	
	item_id = re.findall('href="/deal-show/(.*?)".*?ItemTextLink">',html,re.S)

	#分别进入每个项目的评论页面，获取详细信息
	i = 0
	for url_item_id_temp in item_id:   
		url_item_id_temp = "http://www.zhongchou.com/deal-topic/" + item_id[i]   #评论页面
		i += 1
		req_item_temp = urllib2.Request(url_item_id_temp,headers = headers)
		html_item_comment_temp = urllib2.urlopen(req_item_temp).read()

		pages_of_comment = re.findall('下一页.*?-p-(.*?)\'.*?</a>',html_item_comment_temp,re.S)  #获取评论总页数
		num = pages_of_comment[0]
		for page_present in range(1,int(num)+1):
			url_item_id = "http://www.zhongchou.com/deal-topic/" + item_id[i] + "-p-" + str(page_present) #评论页面逐页打开
			page_present += 1	
			req_item = urllib2.Request(url_item_id,headers = headers)
			html_item_comment = urllib2.urlopen(req_item).read()
		
			#评论
			comments = re.findall('</span></p>.*?<p>(.*?)</p>',html_item_comment,re.S)
			file = open("d:\\PYTHONexercise\\data\\item_comments.txt","a")
			file.write('\n'.join(comments))
			file.write('\n')
			file.close()
		
			#评论者的主页链接
			commentor_id_href = re.findall('<a.*?href="(.*?)".*?class="cyclo-img01">',html_item_comment,re.S)
			file = open("d:/PYTHONexercise/data/commentor_id_href.txt","a")
			file.write('\n'.join(commentor_id_href))
			file.write('\n')
			file.close()	



		
	
#####    FINE    #####	
#   项目名称
#	item = re.findall('class="btnLink.*?ItemTextLink">(.*?)</a>',html,re.S)
#	file = open("d:\\PYTHONexercise\\data\\zhongchoukeji_item.txt","a")
#	file.write('\n'.join(item))
#	file.close()

#   项目简介
#	brief_introduction = re.findall('<img.*?src="".*?alt="(.*?)"/>',html,re.S)
#	file = open("d:/PYTHONexercise/data/zhongchoukeji_brief_introduction.txt","a")
#	file.write('\n'.join(brief_introduction))
#	file.close()

#   最低出资金额
#	startup_capital = re.findall('<span.*?class="FtSpan"><b>(.*?)</b>',html,re.S)
#	file = open("d:/PYTHONexercise/data/zhongchoukeji_startup_capital.txt","a")
#	file.write('\n'.join(startup_capital))
#	file.close

#   筹资进度
#	progress = re.findall('<span.*?class="ScS(.*?)</b>',html,re.S)
#	file = open("d:/PYTHONexercise/data/zhongchoukji_progress.txt","a")
#	file.write('\n'.join(progress))
#	file.close