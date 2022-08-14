from scrapy.crawler import CrawlerProcess
from settings import scrapy_settings
import futbolenlatv

process = CrawlerProcess(scrapy_settings)
process.crawl(futbolenlatv.ScrapySite)
process.start()
