# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ImagesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = table = 'images'
    #  分别代表 MongoDB 存储的 Collection 名称和 MySQL 存储的表名称
    id    = Field()     # 图片 ID
    url   = Field()     # 链接
    title = Field()     # 标题
    thumb = Field()     # 缩略图
