from scrapy.crawler import CrawlerProcess
from functions.todo import deleteExpiredTasks
from settings import scrapy_settings
import futbolenlatv

# Scrapear partidos
process = CrawlerProcess(scrapy_settings)
process.crawl(futbolenlatv.ScrapySite)
process.start()

# Eliminar partidos terminados
deleteExpiredTasks()
