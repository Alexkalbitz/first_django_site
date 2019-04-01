import sys
try:
    import scrapy
except ImportError:
    raise ImportError(sys.path)
import json
from first_test.crawler.mytest.mytest.spiders.httpconnect import send_data






class ZeitSpider(scrapy.Spider):
    name = 'zeit'
    allowed_domains = ['zeit.de']
    start_urls = ['https://zeit.de/']
    print


    def parse(self, response):
        data = {}
        div = response.xpath('//div[contains(@role, "main")]')
        print
        for headline in response.css("h2"):
            site = 'http://www.zeit.de'
            title = headline.css('a::attr(title)').extract()
            link = headline.css('a::attr(href)').extract()
            if len(link) == 0:
                continue
            else:
                if link[0].startswith(site) == True:
                    c = {title[0]:link[0]}
                    data.update(c)
                    print(c)
                else:
                    continue
        my_json = json.dumps(data)
        send_data(my_json)







