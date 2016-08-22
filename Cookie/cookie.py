#-*-coding:utf8-*-
#created by 10412

import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value



#运行结果：
# Name = BAIDUID
# Value = 1F3B6E7D64A89D819027AD367835516A:FG=1
# Name = BIDUPSID
# Value = 1F3B6E7D64A89D819027AD367835516A
# Name = H_PS_PSSID
# Value = 1426_17758_17945_19861_11546_20857_20837_20780
# Name = PSTM
# Value = 1471833707
# Name = BDSVRTM
# Value = 0
# Name = BD_HOME
# Value = 0
