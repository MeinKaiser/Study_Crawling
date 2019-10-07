# -*- coding: utf-8 -*-
import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    # allowed_domains = ['http://www.gmarket.co.kr/Bestsellers']
    start_urls = ['http://www.gmarket.co.kr/Bestsellers/','https://www.naver.com']

    def parse(self, response):
        print(response.url)
