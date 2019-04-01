import sys
try:
    import scrapy
except ImportError:
    raise ImportError(sys.path)
import json
from first_test.crawler.mytest.mytest.spiders.httpconnect import send_data







class JungefreiheitSpider(scrapy.Spider):
    name = 'jungefreiheit'
    allowed_domains = ['jungefreiheit.de/']
    start_urls = ['https://jungefreiheit.de//']

    def parse(self, response):
        data = {}
        for headline in response.css('h2'):
            title = headline.css('a::text').extract_first()
            link = headline.css('a::attr(href)').extract_first()
            a = {title:link}
            data.update(a)
        print(data)
        my_json = json.dumps(data)
        send_data(my_json)










