# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MdpiPipeline(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.mongo_client.mdpi#指定数据库
        self.connection = self.db.agent#指定数据集


    def process_item(self, item, spider):
        # print('##########')
        # print(item)
        # print('##########')
        # print(type(item))  <class 'items.MdpiItem'>
        # print('##########')
        self.connection.insert_one(dict(item))
        return item