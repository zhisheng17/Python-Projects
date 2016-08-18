#-*-coding:utf8-*-
#created by 10412

import urllib2
request = urllib2.Request("http://blog.csdn.net/cqcre")
try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
    print e.reason

#运行结果：
# 403
# Forbidden