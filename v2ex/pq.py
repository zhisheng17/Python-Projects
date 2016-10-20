#-*-coding:utf8-*-
#created by 10412

#保存为pyquery.py文件就会报错：from pyquery import PyQuery ImportError: cannot import name PyQuery，改成pq.py就好了

from pyquery import PyQuery

if __name__ == '__main__':
    q = PyQuery(open('v2ex.html').read())


    print q('title').html()


    for each in q('div.inner>a').items():
        if each.attr.href.find('tab') > 0:
            print 1, each.attr.href

    for each in q('#Tabs>a').items():
        print 2, each.attr.href

    # > 代表cell下一个标签一定要带上a
    for each in q('.cell>a[href^="/go/"]').items():
        print 3, each.attr.href

    # 空格 表示a只要包含在cell这个标签下面就可以了
    for each in q('.cell a[href^="/go/"]').items():
        print 4, each.attr.href

    #获取每个帖子的标题
    for each in q('span.item_title>a').items():
        print 5, each.html()


    #获取每个发帖人头像图片url
    # for each in q('a>img.avatar').items():
    #     print 6, each.html()

