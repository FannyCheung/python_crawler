# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem

class DmozSpider(Spider):	#�̳�scrapy.Spider��
	name = "dmoz"
	allow_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self,response):
		sel = Selector(response)	#ʵ����һ���µ�Selector����
		sites = sel.xpath('//ul[@class="directory-url"]/li')
		items = [] 
		for site in sites:
			item = DmozItem()
			item['title'] = site.xpath('a/text()').extract()
			item['link'] = site.xpath('a/@href').extract()
			item['desc'] = site.xpath('text()').extract()
			items.append(item)
		
		return items
	
'''	
	def parse(self,response):
		filename = response.url.split("/")[-2]
		with open(filename,'wb') as f:
			f.write(response.body)
'''
			

			
			
			
			
			
