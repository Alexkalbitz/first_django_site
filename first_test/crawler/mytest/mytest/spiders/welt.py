import sys
try:
    import scrapy
except ImportError:
    raise ImportError(sys.path)
import json
from first_test.crawler.mytest.mytest.spiders.httpconnect import send_data






class WeltSpider(scrapy.Spider):
    name = 'welt'
    allowed_domains = ['welt.de']
    start_urls = ['https://welt.de/']
    print
    def parse(self, response):
        data={}
        for headline in response.css("h4"):
            a = 'https://welt.de'
            b = headline.css('a::attr(data-linker-href)').extract()
            if len(b) == 0:
                continue
            else:
                c=b[0]
                if c.startswith('/'):
                    link = a+b[0]
            head = headline.css('div::text').extract_first()
            c = {head:link}
            data.update(c)
        print(data)
        my_json = json.dumps(data)
        send_data(my_json)


