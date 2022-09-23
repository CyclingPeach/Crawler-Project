import re
from scrapy import Request, Spider
import pymongo
import requests

class HospitalSpider(Spider):
    name = 'hospital'
    allowed_domains = ['www.medindia.net']
    start_urls = ['https://www.medindia.net']

    def parse(self, response):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db     = self.client['indianhospital']
        self.col    = self.db['hospital']
        self.hospitals = self.col.find({'hospital_belong_province':'Andaman And Nicobar Islands'})
        for hospital in self.hospitals:
            hospital_name = hospital['hospital_name']
            hospital_href = hospital['hospital_href']
            try:
                res = requests.get('http://localhost:5555/random')
                if res.status_code == 200:
                    proxy = 'http://'+res.text
                    yield Request(
                        url      = hospital_href,
                        meta     = {
                            'proxy'                : proxy,
                            'name_by_hospital_col' : hospital_name,
                        },
                        callback = self.parse_detail_info,
                    )
            except:
                pass
        
    def parse_detail_info(self, response):
        if response.status == 200:
            name_by_hospital_col = response.meta['name_by_hospital_col']
            print('*'*50)
            print(response.meta['proxy'])
            print(name_by_hospital_col)
            print('-'*50)
            # hospital_name = response.xpath('//div[@class="mi-bg-1"]/../h2/text()').re_first('Address of (.*)')
            # hospital_address       = ', '.join(response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p[1]//text()').re('\s*(\w.*\w)\s*,*'))
            # hospital_director      = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Director")]/../text()').re_first('\s*(\w.*\w)\s*')
            # hospital_email         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Email")]/../span/text()').re_first('\s*(\w.*\w)\s*')
            # hospital_phone         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Phone")]/../span/text()').re_first('\s*(\w.*\w)\s*')
            # hospital_mobile        = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Mobile")]/../span/text()').re_first('\s*(\w.*\s)\s*')

            # hospital_detail_info = {
            #     'hospital_name'    : hospital_name,
            #     'hospital_address' : hospital_address,
            #     'hospital_director': hospital_director,
            #     'hospital_email'   : hospital_email,
            #     'hospital_phone'   : hospital_phone,
            #     'hospital_mobile'  : hospital_mobile,
            #     'hospital_href'    : None,
            #     'hospital_status'  : None,
            # }

