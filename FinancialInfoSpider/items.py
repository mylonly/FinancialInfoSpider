# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinancialinfospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass





class ArticleItem(scrapy.Item):
    title = scrapy.Field()    #文章标题
    source = scrapy.Field()   #文章来源
    pub_time = scrapy.Field() #发布时间
    content = scrapy.Field()  #文章正文
    image = scrapy.Field()    #文章图片

