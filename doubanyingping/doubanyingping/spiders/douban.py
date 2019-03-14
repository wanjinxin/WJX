# -*- coding: utf-8 -*-
import scrapy
import json
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']
    org_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&' \
              'sort=recommend&page_limit=500&page_start=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/69.0.3497.92 Safari/537.36'
    }
    # f = open('doubanyingping.txt', 'w', encoding='utf-8')
    dr = re.compile(r'<[^>]+>', re.S)

    def start_requests(self):
        yield scrapy.Request(self.org_url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        msg = json.loads(response.text)
        # print(msg)
        for info in msg['subjects']:
            # print(info)
            next_url = info['url']
            # print(next_url)
            yield scrapy.Request(next_url, callback=self.parse_movie, headers=self.headers)

    def parse_movie(self, response):
        info = response.css('div.article')
        # print(info)
        director = info.css('#info > span:nth-child(1) > span.attrs > a::text').extract_first()
        # print(director)
        screenwriter = info.css('#info > span:nth-child(3) > span.attrs >a::text').extract()
        # print(screenwriter)
        actor = self.dr.sub('', info.css('#info > span.actor > span.attrs').extract()[0])
        # actor = info.css('#info > span.actor::text').extract()
        print(actor)



