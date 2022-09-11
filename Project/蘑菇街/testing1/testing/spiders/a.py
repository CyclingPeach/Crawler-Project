# -*- coding: utf-8 -*-
from itertools import product
import scrapy
from lxml import etree
from urllib import request
from unicodedata import category
from testing.items import ShopItem


website = 'a'

class ASpider(scrapy.Spider):
    name = website

    @classmethod
    def update_settings(cls, settings):
        custom_debug_settings = getattr(cls, 'custom_debug_settings' if getattr(cls, 'is_debug', False) else 'custom_settings', None)
        settings.setdict(custom_debug_settings or {}, priority='spider')

    def __init__(self, **kwargs):
        super(ASpider, self).__init__(**kwargs)
        self.counts = 0
        setattr(self, 'author', "")

    is_debug = True
    custom_debug_settings = {
        'MONGODB_COLLECTION': website,
        'CONCURRENT_REQUESTS': 4,
        'DOWNLOAD_DELAY': 1,
        'LOG_LEVEL': 'DEBUG',
        'COOKIES_ENABLED': False,
        'DOWNLOADER_MIDDLEWARES': {
            'testing.middlewares.TestingUserAgentMiddleware': 100,
        },
        'ITEM_PIPELINES': {
            'testing.pipelines.TestingPipeline': 300,
        },
    }

    def start_requests(self):
        url = "https://www.nastygal.com/gb/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        category_href = response.xpath('//ul[@id="main-menu"]/li/a/@href').getall()[:-1]
        for href in category_href:
            category_page_url = response.urljoin(href)
            yield scrapy.Request(url=category_page_url, callback=self.parse_list)

    def parse_list(self, response):
        page_product_href = response.xpath('//div[@class="b-product_tile-container"]/div/h3/a/@href').getall()
        for product_href in page_product_href[:2]:  # 每个品类爬取5个商品
            if product_href is not None:
                product_url = response.urljoin(product_href)
                yield scrapy.Request(url=product_url, callback=self.parse_detail)
        # next_page = response.css('div.b-load_more a::attr(href)').get()
        # yield scrapy.Request(url=next_page, callback=self.parse_list)
    
    def parse_detail(self, response):
        item = ShopItem()
        print('进入到详情页')
        main = response.xpath('//main')
        item['name']           = main.xpath('./h1/text()').get().strip()
        item['detail_cat']     = response.css('ol.b-breadcrumbs-list li:nth-last-child(2) a span::text').get()
        item['original_price'] = main.css('div.b-product_details-price .b-price .m-old::text').getall()[0].strip()
        item['current_price']  = main.css('div.b-product_details-price .b-price .m-new::text').getall()[0].strip()
        description = main.css('div.b-product_details-content p::text').getall() + \
                    main.css('div.b-product_details-content ul::text').getall() + \
                    main.css('div.b-product_details-content ul li::text').getall()
        item['description'] = [des for des in description if des.strip() is not '']
        item['image']          = response.urljoin(response.xpath('//picture[@class="b-product_image"]/img/@src').get())
        item['url']            = response.url

        yield item