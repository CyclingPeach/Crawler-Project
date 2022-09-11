# Define your item pipelines here
'''
import logging

class TestingPipeline:
    def __init__(self):
        self.counts = 0

    def process_item(self, item, spider):
        self.counts += 1
        logging.log(msg=f"成功爬取              {self.counts}              商品", level=logging.INFO)
        # print(item)
'''

from itemadapter import ItemAdapter

class TestingPipeline:
    def process_item(self, item, spider):
        return item