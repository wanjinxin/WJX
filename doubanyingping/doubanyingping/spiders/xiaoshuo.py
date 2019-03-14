# -*- coding: utf-8 -*-
'''
新建文件夹xx,
cd xx
scrapy genspider xiaoshuo www.qidian.com/rank/newvipclick
'''

import scrapy
import re
import json
from ..items import DoubanyingpingItem


class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['www.qidian.com/rank/newvipclick']
    start_urls = ['http://www.qidian.com/rank/newvipclick/']
    # headers一定要带,headers中的user-agent在右键检查network点击第一个点击headers找user-agent，复制下来
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.102 Safari/537.36',
    }
    # cookie根据情况考虑带不带，因为下面抓取信息为空，所以考虑带cookie，cookie返回的是字典形式，网页cookie数据通headers，
    # 根据键值携程dic形式，按情况添加，一般开始不加
    Cookie = {
        '_csrfToken': 'YPJdAvE7XeGWwpSf9HJHmtKmQ7syCCvZ5gTjykdo',
        'newstatisticUUID': '1544163929_1011097386',
        'PAGE_DAILY_MODAL': '7',
        'e1': '%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C47%22%2C%22l1%22%3A5%7D',
        'e2': '%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%2C%22l1%22%3A3%7D'
    }
    # 写入文件xiaoshuo.txt中，'w'覆盖写入
    f = open('xiaoshuo.txt', 'w', encoding='utf-8')

    # 级别最高，自己添加的def start_requests
    def start_requests(self):
        # 网页信息一共25页，观察网址变化，返回的网址是？page=1,2,3,4.....25，即写成for range遍历，构造需要爬取的url
        for i in range(1, 26):
            url = 'http://www.qidian.com/rank/newvipclick?page=' + str(i)
            # 将url传给yield，这里写了5个参数，分别是url，传给方法parse执行，头，cookie，设置不过滤重复项
            # dont_filter最好加上，不然会自动帮你过滤重复的url导致数据的缺失，例如果传入url是唯一的，但是要进行多次的
            # parse方法执行，那他就默认过滤掉只执行一次，此处可忽略，此处url都不一样，参数page递增
            yield scrapy.Request(url, callback=self.parse, headers=self.headers, cookies=self.Cookie, dont_filter=True)

    def parse(self, response):
        # 寻找数据 name，time，content，url，每个数据都是在ul>li标签中，就把所有li取出来
        info_1 = response.css('#rank-view-list > div > ul > li')
        # 遍历，拉取每一个li标签
        for j in info_1:
            # 取名字，最后的extract_first意思是取第一个值，返回的是字符串，如果有多个值，用extract，返回的是列表
            name = j.css('div.book-mid-info > h4 > a::text').extract_first()
            time = j.css('div.book-mid-info > p.update > span::text').extract_first()
            content = j.xpath('.//div[2]/p[2]/text()').extract_first().strip()
            # 主页结束，需要点击爬取详情页，就需要观察详情页的url
            old_url = j.css('div.book-mid-info > h4 > a::attr(href)').extract_first()
            detail_url = 'https:' + old_url
            # 爬取标签，网页返回形式是a|b
            brand_1 = j.css('div.book-mid-info > p.author > a:nth-child(4)::text').extract_first()
            brand_2 = j.css('div.book-mid-info > p.author > span::text').extract_first()
            brand = brand_1 + '|' + brand_2
            bookId = re.findall('\d+', detail_url)[0]
            # 将这个方法取到的值保存下来
            meta = {
                'name': name,
                'time': time,
                'bookId': bookId,
                'content': content,
                'brand': brand
            }
            yield scrapy.Request(detail_url, callback=self.detail_parse, headers=self.headers, cookies=self.Cookie,
                                 meta=meta, dont_filter=True)

    def detail_parse(self, response):
        # 取上个方法的值
        name = response.meta['name']
        time = response.meta['time']
        bookId = response.meta['bookId']
        content = response.meta['content']
        brand = response.meta['brand']
        author = response.css('body > div.wrap > div.book-detail-wrap.center990 > div.book-information.cf > '
                              'div.book-info > h1 > span > a::text').extract_first()
        description = response.css('body > div.wrap > div.book-detail-wrap.center990 > div.book-information.cf > '
                                   'div.book-info > p.intro::text').extract_first()
        # 后需添加，发现爬取评分都是0.0，html返回真实值，但是网页源代码返回0.0，考虑Ajax渲染
        # 寻找ajax地址，右键检查点击network，点击XHR，f5寻找评分数据，继续构造ajax_url
        ajax_url = 'https://book.qidian.com/ajax/comment/index?_csrfToken=YPJdAvE7XeGWwpSf9HJHmtKmQ7syCCvZ5gTjykdo' \
                   '&bookId=' + str(bookId) + '&pageSize=15'
        meta = {
            'name': name,
            'time': time,
            'author': author,
            'content': content,
            'brand': brand,
            'description': description
        }
        yield scrapy.Request(ajax_url, callback=self.rate_parse, headers=self.headers, cookies=self.Cookie,
                             meta=meta, dont_filter=True)
        # 网页源代码返回评分0.0与网页不符，考虑ajax渲染
        # score_1 = response.css('#score1::text').extract_first()
        # score_2 = response.css('#score2::text').extract_first()
        # score = str(score_1) + '.' + str(score_2)
        # print(score)

    def rate_parse(self, response):
        item = DoubanyingpingItem()
        name = response.meta['name']
        time = response.meta['time']
        content = response.meta['content']
        brand = response.meta['brand']
        author = response.meta['author']
        description = response.meta['description']
        # json_loads编译js渲染的文件
        info_3 = json.loads(response.text)
        data = info_3['data']
        score = data['rate']
        item['name'] = name
        yield item
        # print(name, author, brand, score, description, content, time)
        # str_all = str(name) + '\t' + str(author) + '\t' + str(brand) + '\t' + str(score) + '\t' + str(description) +\
        #           '\t' + str(content) + '\t' + str(time) + '\n'
        # self.f.writelines(str_all)


'''
题目是需要爬取http://www.qidian.com/rank/newvipclick/以及每本小说详情页的
小说名name
作者author
标签brand
评分score
描述description
内容content
更新时间time
'''