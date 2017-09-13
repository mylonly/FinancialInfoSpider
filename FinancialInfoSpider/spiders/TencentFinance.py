#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Fri Sep 08 2017
# File: TencentFinance.py
# 
# Description: 
#

import scrapy
from FinancialInfoSpider.items import ArticleItem
from scrapy_splash import SplashRequest
from w3lib.html import remove_tags
import re
from bs4 import BeautifulSoup

class TencentStockSpider(scrapy.Spider):

    name = "TencentStock"

    

    def start_requests(self):

        urls = [
           'http://stock.qq.com/l/stock/ywq/list20150423143546.htm',
        ]

        for url in urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    


    def parse(self,response):

        sel = scrapy.Selector(response)
        links = sel.xpath("//div[@class='qq_main']//ul[@class='listInfo']//li//div[@class='info']//h3//a/@href").extract()
        requests = []
        
        for link in links:
            request = scrapy.Request(link, callback =self.parse_article)
            requests.append(request)
        return requests

    def parse_article(self,response):

        sel = scrapy.Selector(response)

        article = ArticleItem()
        article['url'] = response.url
        article['title'] = sel.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/h1/text()').extract()[0]
        article['source'] = sel.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[2]').xpath('string(.)').extract()[0]
        article['pub_time'] = sel.xpath('//div[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[@class="a_time" or @class="pubTime"]/text()').extract()[0]
        
        html_content = sel.xpath('//*[@id="Cnt-Main-Article-QQ"]').extract()[0]
        article['content'] = self.remove_html_tags(html_content)
        return article


    def remove_html_tags(self,html):
        
        soup = BeautifulSoup(html,"lxml")
        [s.extract() for s in soup('script')]
        [s.extract() for s in soup('style')] 
        
        # re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
        # re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
        # re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
        # re_br=re.compile('<br\s*?/?>')#处理换行
        # re_h=re.compile('</?\w+[^>]*>')#HTML标签
        # re_comment=re.compile('<!--[^>]*-->')#HTML注释
        # s=re_script.sub('',html) #去掉SCRIPT
        # s=re_style.sub('',s)#去掉style
        # s=re_br.sub('\n',s)#将br转换为换行
        # s=re_h.sub('',s) #去掉HTML 标签
        # s=re_comment.sub('',s)#去掉HTML注释
        # #去掉多余的空行
        # blank_line=re.compile('\n+')
        # s=blank_line.sub('\n',s)
        # # s=replaceCharEntity(s)#替换实体
        
        content = ''
        for substring in soup.stripped_strings:
            content = content + substring

        return content       