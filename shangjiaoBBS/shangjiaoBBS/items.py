# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
'''
Function
1、Item 是保存爬取到的数据的容器
2、获取url、发帖版块、发帖人、帖子内容
'''

from scrapy.item import Item,Field

class ShangjiaobbsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()		#url
	forum = Field()		#发帖版块
	poster = Field()	#发帖人
	content = Field()	#帖子内容
