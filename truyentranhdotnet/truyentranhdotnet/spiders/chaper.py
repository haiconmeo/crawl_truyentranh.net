import scrapy


class ChaperSpider(scrapy.Spider):
    name = 'chaper'
    allowed_domains = ['truyentranh.net']
    start_urls = ['https://truyentranh.net/toi-thanh-than-chi-voi-1-mau']

    def parse(self, response):
        for card in response.xpath('//div[has-class("chapter-select")]'):
            title = card.css('a::text').get()
            link = card.css('a::attr(href)').get()
            # chapter =  card.xpath('//ul[has-class("list-chapter")]/li[1]/a/text()').get()
            yield({'title':title,'link':link})
