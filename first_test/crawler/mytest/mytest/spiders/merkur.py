import sys
try:
    import scrapy
except ImportError:
    raise ImportError(sys.path)
import json
from first_test.crawler.mytest.mytest.spiders.httpconnect import send_data






class MerkurSpider(scrapy.Spider):
    name = 'merkur'
    allowed_domains = ['merkur.de']
    start_urls = ['https://www.merkur.de/']
    print
    def parse(self, response):
        data={}
        print
        div = response.xpath('//div[contains(@role, "main")]')
        query = div.css('a')
        for entry in query:
            print
            a = 'https://www.merkur.de/'
            link = entry.css('a::attr(href)').extract_first()
            headline = entry.css('a::text').extract_first()
            print
            if len(headline) == 0 or link.endswith('html') is False:
                continue
            else:
                print

                if link.startswith('/'):
                    completelink = a + link
            c = {head:link}
            data.update(c)
        print(data)
        #my_json = json.dumps(data)
        #send_data(my_json)


