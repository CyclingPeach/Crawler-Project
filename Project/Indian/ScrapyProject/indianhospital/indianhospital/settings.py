BOT_NAME = 'indianhospital'

SPIDER_MODULES = ['indianhospital.spiders']
NEWSPIDER_MODULE = 'indianhospital.spiders'

DOWNLOADER_MIDDLEWARES = {
    'indianhospital.middlewares.RandomUserAgentMiddleware':543,     # 随机 UA
    # 'indianhospital.middlewares.ProxyMiddleware':555,               # 代理池
}

ROBOTSTXT_OBEY = False

PROXY_URL = 'http://localhost:5555/random'