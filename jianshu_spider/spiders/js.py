# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import ArticleItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']
    # 详情页的url写入allow，(.*)表示可有可无,url是由0-9和a-z构成，总共12位,详情页的推荐页面也需要爬，
    # 所以，follow为True，rules作为元组只有一项。加逗号
    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        # item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        # avater = response.xpath("//span[@class='FxYr8x']/a/text()").get()
        # pub_time = response.xpath("//span[@class='_3tCVn5']/time/text()").get()
        url = response.url
        url1 = url.split('?')[0]
        # 以'/'分割为多部份，传入-1取最后一个
        article_id = url1.split('/')[-1]
        content = response.xpath("//article[@class='_2rhmJa']").get()

        # 返回值是一个列表，mysql不支持，需要转化为字符串
        subjects = ','.join(response.xpath("//div[@class='_2Nttfz']/a/span/text()").getall())



        item = ArticleItem(
            title=title,
            origin_url=response.url,
            article_id=article_id,
            content=content,
            subjects=subjects
        )
        yield item


