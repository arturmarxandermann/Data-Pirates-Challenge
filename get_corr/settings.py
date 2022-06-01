BOT_NAME = 'get_corr'
SPIDER_MODULES = ['get_corr.spiders']
NEWSPIDER_MODULE = 'get_corr.spiders'
ROBOTSTXT_OBEY = True
LOG_FILE = "log.txt"
ITEM_PIPELINES = {
    'get_corr.pipelines.RemoveDuplicates': 300,
    'get_corr.pipelines.JsonLineWriterPipeline' : 600
}

DOWNLOAD_DELAY = 1


