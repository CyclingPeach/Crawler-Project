# -*- coding: utf-8 -*-
import scrapy

class ASpider(scrapy.Spider):
    name = 'test'
    def start_requests(self):
        url = "https://www.nastygal.com/gb/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """抓取 所有 类目"""
        category_href = response.xpath('//ul[@id="main-menu"]/li/a/@href').getall()[:-1]
        for href in category_href:
            category_page_url = response.urljoin(href)
            yield scrapy.Request(url=category_page_url, callback=self.parse_list)

    def parse_list(self, response):
        """抓取一个类目中所有的商品"""
        page_product_href = response.xpath('//div[@class="b-product_tile-container"]/div/h3/a/@href').getall()
        for product_href in page_product_href[:2]:  # 每个品类 每页爬取 2 个商品
            if product_href is not None:
                product_url = response.urljoin(product_href)
                yield {'href':product_url}
        
        next_page = response.css('div.b-load_more a::attr(href)').get()
        print('-'*100)
        print(f'【正在抓取{next_page}页的商品】')
        print('-'*100)
        yield scrapy.Request(url=next_page, callback=self.parse_list)

