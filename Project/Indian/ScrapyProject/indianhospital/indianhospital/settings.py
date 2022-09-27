BOT_NAME = 'indianhospital'

SPIDER_MODULES = ['indianhospital.spiders']
NEWSPIDER_MODULE = 'indianhospital.spiders'

DOWNLOADER_MIDDLEWARES = {
    'indianhospital.middlewares.RandomUserAgentMiddleware':543,     # 随机 UA
    'indianhospital.middlewares.ProxyDownloaderMiddleware':100,               # 快代理
}
#注意路径
EXTENSIONS = {
    'indianhospital.myextend.MyExtend': 300,
}
ROBOTSTXT_OBEY = False