import scrapy
import json
import os.path
from ..items import Top20CompaniesItem


class Top20Scrapper(scrapy.Spider):
    name = "top20"
    urls = []

    # retrieving links from companies.json file
    f = open(os.path.dirname(__file__) + '/../../companies.json')
    data = json.load(f)
    for i in data[:20]:
        urls.append(i['link'])

    current = 0
    start_urls = [urls[current]]

    def parse(self, response):

        # items object
        items = Top20CompaniesItem()

        # Retrieving values from response
        name = response.css("div.listuser-header__name::text")[0].extract()
        rank = response.css("span.list-name--rank::text")[0].extract()
        details = response.css("span.profile-stats__text::text").extract()

        # storing values in item
        items['rank'] = rank[1:]
        items['name'] = name
        items['industry'] = details[0]
        items['founded'] = details[1]
        items['headquarters'] = details[2]
        items['country'] = details[3]
        items['ceo'] = details[4]
        items['employees'] = details[5]
        yield items

        # To navigate to further pages
        if self.current < 19:
            self.current += 1
            next_page = self.urls[self.current]
            yield response.follow(next_page, callback=self.parse)
