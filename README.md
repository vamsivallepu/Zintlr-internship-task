# Zintlr Internship Task

1. Create crawler/Scraper using Python [Preferable using Scrapy] to scrape data from https://www.forbes.com/lists/global2000/?sh=45f017755ac0 and save data
in JSON format, attribute-wise.

2. Crawl Top 20 company profiles using the above extracted links based on ranking. Store in a json file with proper formatting.

- The spider to scrawl the given page and scrape the data from tables is written in [this python file](https://github.com/vamsivallepu/Zintlr-internship-task/blob/main/ForbesTop2000/spiders/tableScrapper.py). 
- The spider to scrawl the top 20 companies profile pages and scrape the data is written in [this python file](https://github.com/vamsivallepu/Zintlr-internship-task/blob/main/ForbesTop2000/spiders/top20Scrapper.py ).
- All 2000 companies data is stored in [companies.json](companies.json).
- Data of top 20 companies is stored in [top20_companies.json](top20_companies.json).
