from msilib.schema import Directory
import scrapy

class HospitalSpider(scrapy.Spider):
    name = 'hospital'
    allowed_domains = ['www.medindia.net']
    start_urls = ['https://www.medindia.net/patients/hospital_search/hospital_list.asp?utm_source=topnavigation&utm_medium=desktop&utm_content=&utm_campaign=medindia']

    def parse(self, response):
        """
            印度各个邦的href
            一共 37 个邦
        """
        divs = response.xpath('//ul[@class="list-inline"]/div/div')
        for div in divs:
            # province_name = div.xpath('./li/a/span/text()').get()     # 每个省的名字
            province_href = div.xpath('./li/a/@href').get()     # 每个省所对应的链接（href）
            # yield scrapy.Request(url=province_href, callback=self.parse_province_hospital)
        
        # 只采集一个省(邦)的医院信息
        yield scrapy.Request(url=province_href, callback=self.parse_province_hospital)

            
    def parse_province_hospital(self, response):
        """
            每个邦的所有 医院
            每页最多 25 家医院（需要翻页）
        """
        # province_name = response.xpath('//div[@class="mi-container__fluid"]/h1/text()').re('Find a Hospital in (.*?)')    # 每个省(邦)的名字
        articles = response.xpath('//article[contains(@class, "vert-medium-margin")]')
        for hospital_href in articles.xpath('./div/h3[@class="vert-small-margin"]/a/@href').getall():
            yield scrapy.Request(url=hospital_href, callback=self.parse_hospital)   # 返回 某家医院的链接(href)
        # 翻页（一页仅有25家医院信息，而有些省医院数量超过25家，需要翻页）
        # pagination = response.xpath('//ul[@class="pagination"]/li/a[contains(text(), "Next")]/@href').extract_first()
        # next_page_href = 'https://www.medindia.net/patients/hospital_search/' + pagination
        # print(next_page_href)
        # yield scrapy.Request(url=next_page_href, callback=self.parse_province_hospital)


    def parse_hospital(self, response):
        """
            某家医院的具体信息，包括：
            名字、详细地址、所在市县、所在省份、手机、电话
        """
        hospital_name = response.xpath('//div[@class="mi-bg-1"]/../h2/text()').re_first('Address of (.*)')
        address       = ', '.join(response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p[1]//text()').re('\s*(\w.*\w)\s*,*'))
        director      = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Director")]/../text()').re_first('\s*(\w.*\w)\s*')
        email         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Email")]/../span/text()').re_first('\s*(\w.*\w)\s*')
        phone         = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Phone")]/../span/text()').re_first('\s*(\w.*\w)\s*')
        mobile        = response.xpath('//div[@class="mi-bg-1"]/div/div/div[contains(@class, "report-content")]/p/b[contains(text(), "Mobile")]/../span/text()').re_first('\s*(\w.*\s)\s*')

        # 存储到 hospital.jl文件中
        # 命令 scrapy crawl hospital -o hospital.jl
        # o（小o）对应是将新内容附加到现有文件中，建议使用
        yield {
            'hospital_name':hospital_name,
            'address':address,
            'director':director,
            'email':email,
            'phone':phone,
            'mobile':mobile
        }