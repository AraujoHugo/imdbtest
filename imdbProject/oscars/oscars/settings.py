# Scrapy settings for oscars project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'oscars'

SPIDER_MODULES = ['oscars.spiders']
NEWSPIDER_MODULE = 'oscars.spiders'
ITEM_PIPELINES = {
    'oscars.pipelines.OscarsPipeline': 300,
    'oscars.pipelines.JsonWriter': 800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'oscars (+http://www.yourdomain.com)'
