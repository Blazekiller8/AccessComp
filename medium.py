import scrapy 
from scrapy.crawler import CrawlerProcess
import json

class ArticleScraper(scrapy.Spider):
    name = 'article'
    base_url = 'https://medium.com/featurepreneur'

    header = {

    }