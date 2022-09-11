import json
from urllib.parse import urlencode
from scrapy import Request, Spider
import scrapy
from ..items import ImagesItem

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['https://image.so.com/']

    def start_requests(self):
        data = {'ch':'wallpaper'}
        base_url = 'https://image.so.com/zjl?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImagesItem()
            item['id']    = image.get('id')
            item['url']   = image.get('qhimg_url')
            item['title'] = image.get('title')
            item['thumb'] = image.get('qhimg_thumb')

            yield item