from scrapy.spider import Spider
from scrapy.selector import Selector

from ratings.items import RatingsItem

class SnapshotsSpider(Spider):
    name = "snapshots"
    allowed_domains = ["web.archive.org"]
    start_urls = [
        "http://web.archive.org/web/timemap/http://www.imdb.com/title/tt2333784/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        #sel = Selector(response)
        #sites = sel.xpath('//tr/td')
       	#items = []
       	#aux = ""
        #for site in sites:
         # if site.xpath('a/text()').extract() != [] :
         #   item = OscarsItem()
         #   item['title'] = site.xpath('a/text()').extract()
         #   aux = site.xpath('a/text()').extract()
         #   item['cast'] = site.xpath('a/@title').extract()
         #   items.append(item)
        #  elif site.xpath('strong/text()').extract() != []:
        #    for item in items :
        #      if aux == item['title']:
         #       item['rating'] = site.xpath('strong/text()').extract()
       # return items
