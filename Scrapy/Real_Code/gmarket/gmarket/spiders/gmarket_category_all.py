# -*- coding: utf-8 -*-
import scrapy


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'


    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback = self.parse)
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01', callback = self.parse2)


    def parse(self, response):
        print("parse1")
    
    def parse2(self,response):
        print("parse2")