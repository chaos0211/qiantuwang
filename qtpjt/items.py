# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QtpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    picurl = scrapy.Field()
    # 建立picurl存储图片网址
    picid = scrapy.Field()
    # 建立picid存储图片网址中的用户名
