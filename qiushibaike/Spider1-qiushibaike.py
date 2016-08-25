#-*-coding:utf8-*-
#created by 10412 2016/8/23

#爬取糗事百科的8小时最新页的段子。包含的信息有作者名称，觉得好笑人数，评论人数，发布的内容。
#如果发布的内容中含有图片的话，则过滤图片，内容依然显示出来。

import urllib
import urllib2
import re

#自定义输入爬取的页数
page = raw_input("please enter the page number:")
url = 'http://www.qiushibaike.com/8hr/page/'+ page +'/?s=4880477'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #正则表达式匹配
    pattern = re.compile('<div.*?author.*?>.*?<img.*?>.*?<h2>(.*?)</h2>.*?<div.*?'+
                         'content">(.*?)</div>(.*?)<div.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[2])
        if not haveImg:
            print item[0],item[3],item[4],item[1]
            #item[0]是作者名称  item[3]好笑人数 item[4]评论人数  item[1]内容  item[2]是内容后面的东西，如果含有图片，过滤掉
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason