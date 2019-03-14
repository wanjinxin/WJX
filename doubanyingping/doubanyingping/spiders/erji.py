# -*- coding: utf-8 -*-
import scrapy


class ErjiSpider(scrapy.Spider):
    name = 'erji'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.102 Safari/537.36'
    }
    cookie = {
        'miid': '61642711366245211',
        ' t': 'b667370082fad5afaddb4d8fd1116ea6',
        ' cna': 'c3InFHoTHEMCAXTsqIprHtlK',
        ' thw': 'cn',
        ' hng': 'CN%7Czh-CN%7CCNY%7C156',
        ' UM_distinctid': '16665ccad5f31d-0206e299289ed-661f1574-1fa400-16665ccad6045d',
        ' tg': '0',
        ' enc': 'cyNgXAowskanIaem6TG%2BXn%2FhNoln1e%2FvKWEMTdYIB%2BL62R%2Fcpk53s3AseBloua%2FEH%2FxBgHsXVQf8tF13%2Ff9uKQ%3D%3D',
        ' tracknick': '%5Cu7D2B%5Cu91D11st',
        ' lgc': '%5Cu7D2B%5Cu91D11st',
        ' x': 'e%3D1%26p%3D*%26s%3D0%26c%3D1%26f%3D0%26g%3D0%26t%3D0',
        ' uc3': 'vt3',
        ' _cc_': 'WqG3DMC9EA%3D%3D',
        ' mt': 'ci',
        ' v': '0',
        ' cookie2': '37ab9c22baf9c18a1bce595ab1ddd329',
        ' _tb_token_': 'e69e333dbe37e',
        ' _m_h5_tk': '9959a053c28ab83b40989e52c9d86e13_1544417912975',
        ' _m_h5_tk_enc': 'a46bf25905c0d2047bae010e195007f9',
        ' alitrackid': 'www.taobao.com',
        ' lastalitrackid': 'www.taobao.com',
        ' JSESSIONID': '85D9E7F2048ECF78BE6CCB631D2A612F',
        ' isg': 'BK-vcVZJLytcmCy4QDLigarXPsOzXBP6vslzOsE8WJ4lEM8SySWAxqXKlkCLaNvu',
        ' uc1': 'cookie14'
    }
    f = open('erji.txt', 'w', encoding='utf-8')

    def start_requests(self):
        # 网页一共100页，观察每一页网址的变化，发现变化的参数是s，规律是等差数列，差值为44，构造url
        # string = 'miid=61642711366245211; t=b667370082fad5afaddb4d8fd1116ea6; cna=c3InFHoTHEMCAXTsqIprHtlK; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=16665ccad5f31d-0206e299289ed-661f1574-1fa400-16665ccad6045d; tg=0; enc=cyNgXAowskanIaem6TG%2BXn%2FhNoln1e%2FvKWEMTdYIB%2BL62R%2Fcpk53s3AseBloua%2FEH%2FxBgHsXVQf8tF13%2Ff9uKQ%3D%3D; tracknick=%5Cu7D2B%5Cu91D11st; lgc=%5Cu7D2B%5Cu91D11st; x=e%3D1%26p%3D*%26s%3D0%26c%3D1%26f%3D0%26g%3D0%26t%3D0; uc3=vt3=F8dByR1TNNuxJXBD9x0%3D&id2=UUpprPuztKT%2FpA%3D%3D&nk2=tNCDDLrTbg%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; _cc_=WqG3DMC9EA%3D%3D; mt=ci=-1_0; v=0; cookie2=37ab9c22baf9c18a1bce595ab1ddd329; _tb_token_=e69e333dbe37e; _m_h5_tk=9959a053c28ab83b40989e52c9d86e13_1544417912975; _m_h5_tk_enc=a46bf25905c0d2047bae010e195007f9; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=85D9E7F2048ECF78BE6CCB631D2A612F; isg=BK-vcVZJLytcmCy4QDLigarXPsOzXBP6vslzOsE8WJ4lEM8SySWAxqXKlkCLaNvu; uc1=cookie14=UoTYMhq%2B1jvm4g%3D%3D'
        # a = string.split(';')
        # print(a)
        # for i in a:
        #     j = i.split('=')
        #     k = j[0]
        #     z = j[1]
        #     print("'"+k+"'" + ':' + "'"+z+"'"+',')

        for s in range(0, 4357, 44):
            url = 'https://s.taobao.com/search?spm=a21bo.2017.201856-fline.11.5af911d9BqIQ6t&q=%E8%80%B3%E6%9C%BA&' \
                  'refpid=420463_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f67&bcoffset=0' \
                  '&p4ppushleft=3%2C44&s=' + str(s)
            # 找到了url，传入parse方法进行执行
            yield scrapy.Request(url, callback=self.parse, headers=self.headers, dont_filter=True)

    def parse(self, response):
        info = response.css('#mainsrp-itemlist > div > div > div:nth-child(1) > div')
        print(info)
