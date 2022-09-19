import requests
from scrapy import Request, Spider

class HospitalSpider(Spider):
    name = 'hospital'
    allowed_domains = ['www.medindia.net']
    start_urls = ['https://www.medindia.net/patients/hospital_search/hospital_list.asp?utm_source=topnavigation&utm_medium=desktop&utm_content=&utm_campaign=medindia']

    """结果：返回所有邦(省)的链接"""
    def parse(self, response):
        divs = response.xpath('//ul[@class="list-inline"]/div/div')
        for div in divs:
            # province_name = div.xpath('./li/a/span/text()').get()     # 每个省的名字
            province_href = div.xpath('./li/a/@href').get()     # 每个省所对应的链接（href）
            yield Request(
                url=province_href, 
                callback=self.parse_province_hospital
            )

    """
    结果：
        返回某一邦(省)的所有医院链接（翻页）
        不翻页的话最多有 37(邦) * 25(医院数量/页) = 925 条医院数据（假设每个邦至少有一页(25家)的医院）
        翻译的话
    """
    def parse_province_hospital(self, response):
        # province_name = response.xpath('//div[@class="mi-container__fluid"]/h1/text()').re('Find a Hospital in (.*?)')    # 每个省(邦)的名字
        for hospital_href in response.xpath('//h3[@class="vert-small-margin"]/a/@href').getall():
            yield Request(
                url=hospital_href,
                callback=self.parse_hospital
            )
    
        # 翻页
        # pagination = response.xpath('//ul[@class="pagination"]/li/a[contains(text(), "Next")]/@href').get()
        # next_page_href = 'https://www.medindia.net/patients/hospital_search/' + pagination
        # print(next_page_href)
        # yield Request(
        #     url=next_page_href,
        #     callback=self.parse_province_hospital
        # )

    """返回每家医院的具体信息（名字、详细地址、医生、邮箱、手机、电话）"""
    def parse_hospital(self, response):
        hospital_name = response.xpath('//div[@class="mi-bg-1"]/../h2/text()').re_first('Address of (.*)')
        address       = ', '.join(response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p[1]//text()').re('\s*(\w.*\w)\s*,*'))
        director      = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Director")]/../text()').re_first('\s*(\w.*\w)\s*')
        email         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Email")]/../span/text()').re_first('\s*(\w.*\w)\s*')
        phone         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Phone")]/../span/text()').re_first('\s*(\w.*\w)\s*')
        mobile        = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Mobile")]/../span/text()').re_first('\s*(\w.*\s)\s*')

        yield {
            'hospital_name':hospital_name,
            'address':address,
            'director':director,
            'email':email,
            'phone':phone,
            'mobile':mobile
        }
