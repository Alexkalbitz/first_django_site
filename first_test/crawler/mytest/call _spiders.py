from mytest.spiders import (merkur, jungefreiheit, welt, zeit, sueddeutsche)
from scrapy.crawler import CrawlerProcess


def let_em_crawl1():
    process = CrawlerProcess()
    #put all the crawlers here
    process.crawl(merkur.MerkurSpider)
    #process.crawl(welt.WeltSpider)
    #process.crawl(jungefreiheit.JungefreiheitSpider)
    #process.crawl(zeit.ZeitSpider)
    #process.crawl(sueddeutsche.SueddeutscheSpider)
    #start the crawlers
    process.start()


let_em_crawl1()
