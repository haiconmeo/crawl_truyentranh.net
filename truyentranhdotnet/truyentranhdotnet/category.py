import scrapy


class TruyentranhdotnetCategory(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    
    # pass