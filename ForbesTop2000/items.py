# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# items class to store all companies data
class ForbesTop2000Item(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    sales = scrapy.Field()
    profit = scrapy.Field()
    assets = scrapy.Field()
    market_value = scrapy.Field()
    link = scrapy.Field()


# items class to store top 20 companies data
class Top20CompaniesItem(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    industry = scrapy.Field()
    founded = scrapy.Field()
    headquarters = scrapy.Field()
    country = scrapy.Field()
    ceo = scrapy.Field()
    employees = scrapy.Field()
