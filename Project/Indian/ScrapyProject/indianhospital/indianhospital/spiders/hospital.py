from msilib.schema import Directory
import scrapy

class HospitalSpider(scrapy.Spider):
    name = 'hospital'
    allowed_domains = ['www.medindia.net']
    # start_urls = ['https://www.medindia.net/patients/hospital_search/hospital_list.asp?utm_source=topnavigation&utm_medium=desktop&utm_content=&utm_campaign=medindia']
    start_urls = ['https://www.medindia.net/patients/hospital_search/a-i-i-m-s-hospital-delhi-60897-1.htm']

    def parse(self, response):
        # self.logger.debug(response.text)
        print('-'*50)
        """
            印度各个邦的href
            一共 37 个邦
        """
        # print(len(response.xpath('//ul[@class="list-inline"]/div/div/li/a/@href').extract()))
        # print(response.xpath('//ul[@class="list-inline"]/div/div/li/a/@href').extract())
        

        """
            每个邦的所有 医院
            每页最多 25 家医院（翻页）
        """
        # articles = response.xpath('//article[contains(@class, "vert-medium-margin")]')
        # print(len(articles))  # 25
        # 翻页
        # pagination = response.xpath('//ul[@class="pagination"]/li/a[contains(text(), "Next")]/@href').extract_first()
        # next_page_href = 'https://www.medindia.net/patients/hospital_search/' + pagination
        # print(next_page_href)

        """
            某家医院的具体信息，包括：
            名字、详细地址、所在市县、所在省份、手机、电话
        """
        hospital_name = response.xpath('//div[@class="mi-bg-1"]/../h2/text()').re_first('Address of (.*)')
        # address       = ', '.join(response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p[1]//text()').re('\s*(\w.*\w)\s*,*'))
        # director      = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Director")]/../text()').re_first('\s*(\w.*\w)\s*')
        # email         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Email")]/../span/text()').re_first('\s*(\w.*\w)\s*')
        # phone         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Phone")]/../span/text()').re_first('\s*(\w.*\w)\s*')
        # mobile        = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Mobile")]/../span/text()').re_first('\s*(\w.*\s)\s*')

        print(hospital_name)
        print('-'*50)
