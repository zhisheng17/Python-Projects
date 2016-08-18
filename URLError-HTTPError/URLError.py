#-*-coding:utf8-*-
#created by 10412

# URLError可能产生的原因：
#
# 网络无连接，即本机无法上网
# 连接不到特定的服务器
# 服务器不存在
# 在代码中，我们需要用try-except语句来包围并捕获相应的异常。


import urllib2


request = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

#运行结果：[Errno 11002] getaddrinfo failed