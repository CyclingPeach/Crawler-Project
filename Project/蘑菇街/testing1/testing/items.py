# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ShopItem(scrapy.Item):
    name            = scrapy.Field() # 商品名字
    detail_cat      = scrapy.Field()  # 商品的类目，home/clothes/。。。。
    original_price  = scrapy.Field()  # 原价
    current_price   = scrapy.Field()  # 现价
    image           = scrapy.Field()  # 商品首图
    description     = scrapy.Field()  # 商品功能描述
    url             = scrapy.Field()  # 商品链接