import scrapy
from ..items import ForbesTop2000Item


class CompaniesSpider(scrapy.Spider):
    name = "companies"
    start_urls = [
        "https://www.forbes.com/lists/global2000/?sh=1579a6f95ac0"
    ]

    def parse(self, response):
        # items object
        items = ForbesTop2000Item()

        # getting all table rows
        table_row = response.css("a.table-row")

        # iterate through every row and get corresponding values
        for row in table_row:
            rank = row.css("div.rank::text").extract()
            name = row.css("div.organizationName::text").extract()
            country = row.css("div.country::text").extract()
            sales = row.css("div.revenue::text").extract()
            profit = row.css("div.profits::text").extract()
            assets = row.css("div.assets::text").extract()
            market_value = row.css("div.marketValue::text").extract()
            link = row.css("::attr(href)").get()

            # storing values in item
            items['rank'] = rank[0][:-1]
            items['name'] = name[0]
            items['country'] = country[0]
            items['sales'] = sales[0]
            items['profit'] = profit[0]
            items['assets'] = assets[0]
            items['market_value'] = market_value[0]
            items['link'] = link

            yield items
