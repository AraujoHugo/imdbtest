from scrapy.spider import Spider
from scrapy.selector import Selector

from oscars.items import OscarsItem

class OscarsSpider(Spider):
    name = "oscars"
    allowed_domains = ["imdb.com"]
    start_urls = [
        "http://imdb.com/chart/top"
    ]

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
        sel = Selector(response)
        sites = sel.xpath('//tr/td')
       	items = []
       	aux = ""
        for site in sites:
          if site.xpath('a/text()').extract() != [] :
            item = OscarsItem()
            item['title'] = site.xpath('a/text()').extract()
            aux = site.xpath('a/text()').extract()
            item['cast'] = site.xpath('a/@title').extract()
            items.append(item)
          elif site.xpath('strong/text()').extract() != []:
            for item in items :
              if aux == item['title']:
                item['rating'] = site.xpath('strong/text()').extract()
        return items



