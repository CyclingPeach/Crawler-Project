from cgitb import text
from queue import Queue
from winreg import QueryReflectionKey
import scrapy
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print(type(response))
        quotes = response.css('.quote')
        for quote in quotes:
            item = TutorialItem
            item['text']   = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags']   = quote.css('.tag .tag::text').extract()
            yield item
        next = response.css('.pager .next a::attr(href)').extract_fisrt()
        url  = response.urljoin(next)   # 将相对URL构造成一个绝对的URL
        yield scrapy.Request(url=url, callback=self.parse)