import sys
try:
    import scrapy
except ImportError:
    raise ImportError(sys.path)
import json
from first_test.crawler.mytest.mytest.spiders.httpconnect import send_data






class SueddeutscheSpider(scrapy.Spider):
    name = 'sueddeutsche'
    allowed_domains = ['sueddeutsche.de']
    start_urls = ['http://www.sueddeutsche.de/']

    def parse(self, response):
        data = {}
        div = response.xpath('//div[contains(@id, "sitecontent")]')
        query = div.css('a')
        for entry in query:
            site = 'http://www.sueddeutsche.de/'
            title = entry.css('em').extract_first()
            link = entry.css('a::attr(href)').extract_first()
            if title == None or len(title) < 1:
                continue
            else:
                if link.startswith('http://www.sueddeutsche.de/') == True:
                    a1 = title.replace('<em>', '')
                    a2 = a1.replace('</em>', '')

                    c = {a2:link}
                    data.update(c)
                else:
                    continue
            print(data)
        print
        my_json = json.dumps(data)
        send_data(my_json)


