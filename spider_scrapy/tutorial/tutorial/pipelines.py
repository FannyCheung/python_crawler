# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class FilterWordsPipeline(object):	#过滤掉含“politics”、“religion”字的网页内容
	words_to_filter = ['politics','religion']
	
	def process_item(self,item,spider):
		for word in self.words_to_filter:
			if word in unicode(item['desc']).lower():
				raise DropItem("Contains forbidden word: %s" % word)
			else:
				return item
		
		









		