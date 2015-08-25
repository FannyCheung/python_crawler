# -*- coding: utf-8 -*-

from scrapy.item import Item, Field  
class TencentItem(Item):  
    name = Field()                # 职位名称  
    catalog = Field()             # 职位类别  
    workLocation = Field()        # 工作地点  
    recruitNumber = Field()       # 招聘人数  
    detailLink = Field()          # 职位详情页链接  
    publishTime = Field()         # 发布时间  