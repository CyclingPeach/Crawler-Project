import pymongo

class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db  = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url = crawler.settings.get('MONGO_URL'),
            mongo_db  = crawler.settings.get('MONGO_DB')
        )
    
    def open(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db     = self.client[self.mongo_db]
    
    def process_item(self, item, spider):
        self.db[item.collection].insert_one(dict(item))
        return item

    def close(self, spider):
        self.client.close()
        