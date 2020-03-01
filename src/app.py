# coding: utf-8
from crawler.spider import KabumSpider
from dataclass.Produto import CelularXiaomi
from scrapy.crawler import CrawlerProcess


produtoCelularXiaomi = CelularXiaomi()

spiderKabum = KabumSpider()
spiderKabum.start_urls.append(produtoCelularXiaomi.uri[1])

process = CrawlerProcess()
process.crawl(spiderKabum.__class__)
process.start() # the script will block here until the crawling is finished

# runtime = Runtime()
# runtime.run(produtoCelularXiaomi)


 