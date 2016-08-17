#coding=utf-8
import urllib
#在python3.3里面，用urllib.request代替urllib2
import urllib.request
import re

url = "http://tieba.baidu.com/p/2460150866"
page = urllib.request.urlopen(url)
html = page.read()
print(html)    #python3中只能用print(html) python2中能写print html

#正则匹配
reg = r'src="(.+?\.jpg)" pic_ext'
imgre = re.compile(reg)
imglist = re.findall(imgre, html.decode('utf-8'))
x = 0
print("start dowload pic")
for imgurl in imglist:
	print(imgurl)
	resp = urllib.request.urlopen(imgurl)
	respHtml = resp.read()
	picFile = open('%s.jpg' % x, "wb")
	picFile.write(respHtml)
	picFile.close()
	x = x+1
print("done")