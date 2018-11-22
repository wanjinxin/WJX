# -*- coding: utf-8 -*-
import scrapy
from books.items import BooksItem
from scrapy.linkextractor import LinkExtractor


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    f = open('Booklist1.txt', 'w', encoding='utf-8')

    def parse(self, response):
        for info in response.css('.product_pod'):
            item = BooksItem()
            # print(info)
            item['name'] = info.css('h3>a::attr(title)').extract_first()
            # name = info.xpath('./h3/a/@title').extract_first()
            # print(name)
            item['price'] = info.css('.product_price .price_color::text').extract_first()
            # price = info.xpath('//p[@class="price_color"]/text()').extract()
            # print(price)
            yield item
            bookstr = item['name'] + '\t' + item['price'] + '\n'
            self.f.write(bookstr)
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)
        '''next_url = response.css('.pager .next>a::attr(href)').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)'''





