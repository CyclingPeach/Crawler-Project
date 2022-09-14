# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item


class IndianhospitalItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hospital_name = Item.fields()
    address       = Item.fields()
    director      = Item.fields()
    email         = Item.fields()
    phone         = Item.fields()
    mobile        = Item.fields()

