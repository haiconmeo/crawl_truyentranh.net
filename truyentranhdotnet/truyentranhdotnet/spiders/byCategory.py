import scrapy


class BycategorySpider(scrapy.Spider):
    name = 'byCategory'
    allowed_domains = ['truyentranh.net']
    start_urls = ['https://truyentranh.net/category/manga']
    def start_requests(self):                                                   
        for url in self._url_list:                                              
            yield scrapy.Request(url = url, callback = self.parse) 
    def parse(self,response):
        page = response.xpath('//a[has-class("page-link")]')
        late = int(page[-1].css('a::attr(href)').get().split('page=')[-1])
        for i in range(1,late+1):
            yield scrapy.Request('https://truyentranh.net/category/manga?page='+str(i),callback=self.parse_2)
    def parse_2(self, response):
        for card in response.xpath('//div[has-class("card")]'):
            title = card.css('a::attr(title)').get()
            link = card.css('a::attr(href)').get()
            # chapter =  card.xpath('//ul[has-class("list-chapter")]/li[1]/a/text()').get()
            yield({'title':title,'link':link})
