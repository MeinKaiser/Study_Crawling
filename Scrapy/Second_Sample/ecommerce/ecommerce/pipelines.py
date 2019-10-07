# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class EcommercePipeline(object):
    def process_item(self, item, spider):
        print(item)
        if int(item['price']) > 20000:
            return item
        else:
            raise DropItem("ByeBye")
        return item
