BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    # 'tutorial.pipelines.TextPipeline': 300,
    'tutorial.pipelines.MongoDBPipeline': 400,
}

MONGO_URL = 'localhost'
MONGO_DB  = 'tutorial'