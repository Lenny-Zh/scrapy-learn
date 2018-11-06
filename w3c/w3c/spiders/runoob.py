# -*- coding: utf-8 -*-
import scrapy

from w3c.items import W3CItem 

class RunoobSpider(scrapy.Spider):
    name = 'runoob'
    allowed_domains = ['runoob.com']
    start_urls = ['http://www.runoob.com/html/html-tutorial.html']

    def parse(self, response):
        filename = response.url.split("/")[-2]
        item = W3CItem()
        print "尝试倒入数据"
        print type(item)
        for sel in response.xpath('//a/text()'):
        	item = W3CItem()
        	name = sel.extract()
        	print name
        	item['name'] = name
        	yield item
        	# name = sel.xpath()

        # with open(filename, 'wb') as f:
        #     f.write(response.body)

