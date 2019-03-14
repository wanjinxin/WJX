# -*- coding: utf-8 -*-
import json

import scrapy
from weather.items import WeatherItem


class A2345tianqiSpider(scrapy.Spider):
    name = 'a2345tianqi'
    allowed_domains = ['tianqi.2345.com/wea_history/58362.htm']
    start_urls = ['http://tianqi.2345.com/wea_history/58362.htm/']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    f = open('weather.txt', 'w', encoding='utf-8')

    def start_requests(self):
        date_list = [201801, 201802, 201803, 201804, 201805, 201806, 201807,
                     201808, 201809, 201810, 201811, 201812, 201901]
        for i in date_list:
            url = 'http://tianqi.2345.com/t/wea_history/js/{0}/58362_{0}.js'.format(i)
            yield scrapy.Request(url, callback=self.parse, headers=self.headers, dont_filter=True)

    def turnjson(self, jsonstr):
        dict1 = {
            '{': '{\'',
            ':': '\':',
            ',': ',\'',
            '\'{\'': '{\'',
            '{\'}': '{}'
        }
        for key in dict1:
            jsonstr = jsonstr.replace(key, dict1[key])
        return jsonstr

    def parse(self, response):
        item = WeatherItem()
        html = response.body.decode('GBK')
        str1 = self.turnjson(html.split('var weather_str=')[-1].split(';')[0])
        json1 = json.loads(str1.replace('\'', '"'))
        city = json1['city']
        for tq in json1['tqInfo']:
            try:
                ymd = tq['ymd']
                bWendu = tq['bWendu']
                yWendu = tq['yWendu']
                tianqi = tq['tianqi']
                item['bWendu'] = bWendu
                item['yWendu'] = yWendu
                yield item
                fengxiang = tq['fengxiang']
                fengli = tq['fengli']
                aqi = tq['aqi']
                aqiInfo = tq['aqiInfo']
                aqiLevel = tq['aqiLevel']
                print(city, ymd, bWendu, yWendu, tianqi, fengxiang, fengli, aqi, aqiInfo, aqiLevel)
                str_all = str(city) + '\t' + str(ymd) + '\t' + str(bWendu) + '\t' + str(
                    yWendu) + '\t' + str(tianqi) + '\t' + str(fengxiang) + '\t' + str(
                    fengli) + '\t' + str(aqi) + '\t' + str(aqiInfo) + '\t' + str(aqiLevel) + '\n'
                self.f.writelines(str_all)
            except:
                pass
