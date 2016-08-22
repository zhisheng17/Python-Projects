#-*-coding:utf8-*-
#created by 10412

# 下面我们以我们学校的教育系统为例，利用cookie实现模拟登录，并将cookie信息保存到文本文件中，来感受一下cookie大法吧！

# 注意：密码我改了啊，别偷偷登录本宫的选课系统 o(╯□╰)o

import urllib
import urllib2
import cookielib

filename = 'cookie2.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'user':'jwc',
			'pass':'***'
		})
#登录教务系统的URL
loginUrl = 'http://jwc.ecjtu.jx.cn/mis_o/login.htm'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie2.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是查询第二课堂学分网址
gradeUrl = 'http://jwc.ecjtu.jx.cn:8080/jwcmis/dektxf.jsp'
#请求访问查询第二课堂学分网址
result = opener.open(gradeUrl)
print result.read()