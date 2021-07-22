import scrapy
from truyentranhdotnet.category import TruyentranhdotnetCategory

class MangaSpider(scrapy.Spider):
    name = 'manga'
    allowed_domains = ['truyentranh.net']
    start_urls = ['https://truyentranh.net/category']

    def parse(self, response):
        for categori in response.xpath('//div[has-class("manga-category-item")]'):
            title = categori.css('h5::text').get()
            link = categori.css('a::attr(href)').get()
            yield({'title':title,'link':link})

