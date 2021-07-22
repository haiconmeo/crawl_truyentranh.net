import scrapy


class ContentSpider(scrapy.Spider):
    name = 'content'
    allowed_domains = ['truyentranh.net']
    start_urls = ['https://truyentranh.net/toi-thanh-than-chi-voi-1-mau/chap-001-250693']

    def parse(self, response):
        for card in response.xpath('//div[has-class("page-chapter")]'):
            image = card.css('img::attr(src)').get()
            yield({'title':image})
