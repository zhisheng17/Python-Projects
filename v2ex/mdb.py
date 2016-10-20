#-*-coding:utf8-*-
#created by 10412

import MySQLdb
import random


#测试连接数据库
if __name__ == '__main__':
    db = MySQLdb.connect("localhost", "root", "root", "wenda", charset="utf8")
    try:
        cursor = db.cursor()

        '''
        #插入数据
        sql = 'insert into question(title, content, user_id, created_date, comment_count) values("怎样能够写出一篇10万+的文章出来？", "看到微信公众号好多大V写出的文章阅读量都是这么多，但是不知道自己可以怎么写，需要注意点什么吗？", 14, now(), 0)'
        cursor.execute(sql)
        qid = cursor.lastrowid
        db.commit()
        print qid
        '''

        #查询数据
        sql = 'select * from question order by id desc limit 3'
        cursor.execute(sql)
        for each in cursor.fetchall():
            for row in each:
                print row

        db.commit()
    except Exception, e:
        print e
        db.rollback()
    db.close()

