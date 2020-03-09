# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# ArticleItem需要在js.py中作为模块导入
class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    origin_url = scrapy.Field()
    article_id = scrapy.Field()
    content = scrapy.Field()
    subjects = scrapy.Field()



