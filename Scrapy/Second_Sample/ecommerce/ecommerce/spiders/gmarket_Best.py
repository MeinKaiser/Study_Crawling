# -*- coding: utf-8 -*-
import scrapy
from ecommerce.items import EcommerceItem

class GmarketBestSpider(scrapy.Spider):
    name = 'gmarket_Best'
    # allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['https://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list li > a::text').getall()

        prices = response.css('div.best-list ul li div.item_price div.s-price strong span::text').getall()
        for num ,title in enumerate(titles):
            item = EcommerceItem()
            item['title'] = title
            item['price'] = prices[num].strip().replace("원","").replace(",","")
            #strip으로 띄어쓰기 삭제!
            #replace 함수 기억해두기
            yield item
    