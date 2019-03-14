# -*- coding: utf-8 -*-
import scrapy
import json


class XiciProxySpider(scrapy.Spider):
    name = 'xici_proxy'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/69.0.3497.92 Safari/537.36'
    }
    f = open('list_1.txt', 'w', encoding='utf-8')

    def start_requests(self):
        for i in range(1, 2):
            yield scrapy.Request(url="http://www.xicidaili.com/nn/%s" % i, headers=self.headers)

    def parse(self, response):
        for sel in response.xpath('//table[@id="ip_list"]/tr[position()>1]'):
            ip = sel.css('td:nth-child(2)::text').extract_first()
            port = sel.css('td:nth-child(3)::text').extract_first()
            scheme = sel.css('td:nth-child(6)::text').extract_first().lower()

            url = '%s://httpbin.org/ip' % scheme
            proxy = '%s://%s:%s' % (scheme, ip, port)

            meta = {
                'proxy': proxy,
                'dont_retry': True,

                '_proxy_scheme': scheme,
                '_proxy_ip': ip
            }
            yield scrapy.Request(url, callback=self.check_available, meta=meta, dont_filter=True, headers=self.headers)

    def check_available(self, response):
        proxy_ip = response.meta['_proxy_ip']
        if proxy_ip == json.loads(response.text)['origin']:
            proxy = response.meta['proxy']
            proxy_scheme = response.meta['_proxy_scheme']
            # yield {
            #     'proxy_scheme': response.meta['_proxy_scheme'],
            #     'proxy': response.meta['proxy']
            # }
            print(proxy)
            str = proxy + '\n'
            self.f.write(str)
