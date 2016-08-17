#-*-coding:utf8-*-
import urllib
import urllib2

values={}
values['username'] = "1041218129@qq.com"
values['password']="***12"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl            #打印输出一下url，发现其实就是原来的url加？然后加编码后的参数

#http://passport.csdn.net/account/login?username=1041218129%40qq.com&password=***12