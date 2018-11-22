# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    f = open('quote.txt', 'w', encoding='utf-8')

    def parse(self, response):
        for info in response.css('.quote'):
            name = info.css('.author::text').extract_first()
            # print(name)
            content = info.css('.text::text').extract_first()
            # print(content)
            tags = info.css('.tag::text').extract()
            # print(tags)
            '''yield {
                'name': name,
                'content': content,
                'tags': tags
            }'''
            quotesstr = content + '\t' + name + '\n'
            self.f.write(quotesstr)

        next_url = response.css('.pager .next>a::attr(href)').extract_first()

        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
