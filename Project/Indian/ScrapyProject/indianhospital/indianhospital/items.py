# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item


class IndianhospitalItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name              = Item.fields()
    detail_address    = Item.fields()
    town_and_postcode = Item.fields()
    province          = Item.fields()
    phone             = Item.fields()
    mobile            = Item.fields()

