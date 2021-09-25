from scrapy.crawler import CrawlerProcess
from functions import scrapy

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
    'FEED_EXPORT_ENCODING': 'utf-8',
})
process.crawl(scrapy.ScrapySite)
process.start()