# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector

from ratings.items import RatingsItem

class RatingsSpider(Spider):
    name = "ratings"
    allowed_domains = ["web.archive.org","imdb.com"]
    #rfile = open("timemap", 'r')
    start_urls = [
    #"http://web.archive.org/web/20140414212300/http://www.imdb.com:80/title/tt0133093/"]
    "http://imdb.com/chart/top"]

    #for line in rfile:
     #   cenas = line.split()
      #  start_urls.append("http://web.archive.org/web/"+cenas[1]+"/"+cenas[2])
    

    def parse(self, response):
        #filename = response.url.split("/")[4]
        #open(filename, 'wb').write(response.body)
        sel = Selector(response)
        sites = sel.xpath('//tr/td')
       	items = []
       	#aux = ""
        for site in sites:
            if site.xpath('a/text()').extract() != []:
                aux = site.xpath('a/text()').extract()
                open("cenas.txt", 'w').write(aux[0].encode('utf-8')+"BOOOOOOBS!!!");
                #######WHERE!!!##############################
                #open("cenas", 'wb').write("(.)(.)!");
            else:
                open("cenas", 'wb').write("BOOBS!");
        #open("cenas","wb").close()
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
