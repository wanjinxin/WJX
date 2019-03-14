# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanyingpingPipeline(object):
    def process_item(self, item, spider):
        return item


from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
class TutorialPipeline(object):
    def __init__(self):
        dbargs = dict(
            host = 'localhost',
            db = 'test',
            user = 'root', #replace with you user name
            passwd = 'Wanjinxin415723;', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)


    '''
    The default pipeline invoke function
    '''
    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):
        conn.execute('insert into xiaoshuo(title,author,pub_date,types,tags,view_counts,content) '
                     'values(%s)', (item['name']))



'''
[root@bogon cnblogs]# more pipelines.py
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors

class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('cnblogs.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MySQLStoreCnblogsPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    
    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d
    #将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        linkmd5id = self._get_linkmd5id(item)
        #print linkmd5id
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        conn.execute("""
                select 1 from cnblogsinfo where linkmd5id = %s
        """, (linkmd5id, ))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id))
            #print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            #""", (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated) 
                values(%s, %s, %s, %s, %s, %s)
            """, (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now))
            #print """
            #    insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
            #    values(%s, %s, %s, %s, %s, %s)
            #""", (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now)
    #获取url的md5编码
    def _get_linkmd5id(self, item):
        #url进行md5处理，为避免重复采集设计
        return md5(item['link']).hexdigest()
    #异常处理
    def _handle_error(self, failue, item, spider):
        log.err(failure)
'''