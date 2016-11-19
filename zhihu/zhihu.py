#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-11-19 19:50:10
# Project: zhihu

from pyspider.libs.base_handler import *
import random
import MySQLdb


class Handler(BaseHandler):
    crawl_config = {

        'itag': 'v1',
        'headers': {
            'User-Agent': 'GoogleBot',
            'Host': 'www.zhihu.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
    }

    # 连接数据库
    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', 'root', 'wenda', charset='utf8')

    # 插入问题
    def add_question(self, title, content, comment_count):
        try:
            cursor = self.db.cursor()
            sql = 'insert into question(title, content, user_id, created_date, comment_count) values ("%s","%s",%d, %s, %d)' % (
            title, content, random.randint(1, 10), 'now()', comment_count);
            # print sql
            cursor.execute(sql)
            qid = cursor.lastrowid  # qid是问题的ID
            self.db.commit()
            return qid
        except Exception, e:
            print
            e
            self.db.rollback()

    # 插入评论
    def add_comment(self, qid, comment):  # 根据问题的ID，然后插入对应的评论
        try:
            cursor = self.db.cursor()
            sql = 'insert into comment(content, user_id, entity_id, entity_type, created_date) values ("%s","%d",%d, %d, %s)' % (
            comment, random.randint(1, 10), 1, qid, 1, 'now()');
            # print sql
            cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            print
            e
            self.db.rollback()
        return 0

    # 话题精华页
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.zhihu.com/topic/19550517/top-answers?page=1', callback=self.index_page,
                   validate_cert=False)  # 互联网话题精华回答
        # self.crawl('https://www.zhihu.com/topic/19552330/top-answers?page=1', callback=self.index_page, validate_cert=False)#程序员话题精华回答

    # 通过question_link找到问题的详情页
    # 通过.zm-invite-pager span a实现翻页
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a.question_link]').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)
        for each in response.doc('.zm-invite-pager span a').items():
            self.crawl(each.attr.href, callback=self.index_page,
                       validate_cert=False)  # 找到.zm-invite-pager span a后，继续循环index_page，从而实现翻页把该话题中所有的精华问题都爬取到

    @config(priority=2)
    def detail_page(self, response):
        items = response.doc('div.zm-editable-content clearfix').items  # items  问题的评论
        title = response.doc('span.zm-editable-content').text()  # title  问题的题目
        html = response.doc('#zh-question-detail .zm-editable-content').html()  # html   问题的补充描述
        # 因为有些问题的下面没有补充说明，所以我们要进行判断html是否为空
        if html == None:
            html = ''

        content = html.replace('"', '\\"')
        print
        content

        # 评论下一页是通过Ajax加载的，后期在来弄

        qid = self.add_question(title, content, sum(1 for x in items))
        for each in response.doc('div.zm-editable-content clearfix').items:
            self.add_comment(qid, each.html.replace('"', '\\"'))

        return {
            "url": response.url,
            "title": title,
            "content": content,
        }
