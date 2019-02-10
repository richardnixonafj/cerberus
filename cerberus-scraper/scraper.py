import scrapy


class CerberusSpider(scrapy.Spider):
    name = "cerberus_spider"
    start_urls = ['http://brickset.com/sets/year-2016']
