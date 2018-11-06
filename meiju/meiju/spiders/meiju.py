# -*- coding: utf-8 -*-
import scrapy
from meiju.items import MeijuItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/']

    def parse(self, response):
        movies = response.xpath('//div[@class="list_2"]/ul/li')

        for each_movie in movies:
            item = MeijuItem()
            item['name'] = each_movie.xpath('./a/@title').extract()[0]
            yield item
