# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class WeatherPipeline(object):
    def __init__(self):
        # host = '127.0.0.1'
        # host = '10.8.16.189'
        host = 'localhost'
        port = 27017
        self.client = pymongo.MongoClient(host=host, port=port)

    def process_item(self, item, spider):
        # 创建MONGODB数据库链接
        dbname = 'test'
        mydb = self.client[dbname]

        sheetname = '2345tianqi'
        post = mydb[sheetname]
        post.insert(dict(item))
