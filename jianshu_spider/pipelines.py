# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# from twisted.enterprise import adbapi
class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '你的密码',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        # 把字典中的key、value都传过来
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None


    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'],item['content'],item['origin_url'],item['article_id'],item['subjects']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,title,content,origin_url,article_id,subjects) values(null,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql
