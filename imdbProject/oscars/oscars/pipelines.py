# -*- coding: utf-8 -*- 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import unicodedata as uni

class OscarsPipeline(object):
    def process_item(self, item, spider): 
        try:
        	if float(str(item['rating'])) > 8.5:
        		item['title'] = "WORKS!"
        except KeyError:
        	item['title'] = "FUCK OFF!"

        return item


class JsonWriter(object):
    
    def __init__(self):
        self.file = open('oscars.txt', 'w')

    def process_item(self, item, spider):
        
        try:	
        	line = str(item['title'])+'\n' #json.dumps(dict(item)) + "\n"
        	self.file.write(line)
        except KeyError:
        	self.file.write("")

        return item
