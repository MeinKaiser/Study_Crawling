# -*- coding: utf-8 -*-
import scrapy


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['www.gmarket.co.kr']
    #allowd_domains , 이것만 하겠다!!! 라고 설정해주는 것
    start_urls = ['http://www.gmarket.co.kr/']
    #여러 주소 가능 ㄷㄷ..

    def parse(self, response):
        print(response.text)
