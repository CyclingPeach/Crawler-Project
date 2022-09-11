# Define here the models for your scraped items
#
from distutils.ccompiler import show_compilers
from scrapy import Item, Field

class ProductItem(Item):
    collection = 'products'
    image    = Field()
    price    = Field()
    deal     = Field()
    title    = Field()
    shop     = Field()
    location = Field()
