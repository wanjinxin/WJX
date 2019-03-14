# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmployZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

    jobName = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    backGroup = scrapy.Field()
    salary = scrapy.Field()
    scale = scrapy.Field()
    require = scrapy.Field()
    experience = scrapy.Field()
    enterprise = scrapy.Field()
    detail = scrapy.Field()

    linkUrl = scrapy.Field()
    crawled = scrapy.Field()
    spider = scrapy.Field()



