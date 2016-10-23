# _*_coding:utf-8_*_
import re,urllib


#获取网址url
def get_url(page):
    return 'http://www.budejie.com/video/'+str(page)


#获取源代码html
def get_html(url):
    return urllib.urlopen(url).read() #read读取网页源代码


#下载相对应标题，即视频名字
def download(mp4_url,path):
    #print path     #打印mp4视频的标题
    path="".join(path.split())
    urllib.urlretrieve(mp4_url,'%s.mp4'%(path.decode('utf-8').encode('gbk')))
    print 'ok!!'


#匹配地址  第一：匹配视频地址。第二：匹配标题。
def get_mpl_url(request):
    reg=r'data-mp4="(.*?)"'
    return re.findall(reg,request)


#匹配名称
def get_name(request):
    reg=re.compile(r'<div class="j-r-list-c-desc">(.*?)</div>',re.S)
    return re.findall(reg,request)


#调用
html=get_html(get_url(1))
mp4_url=get_mpl_url(html)
mp4_name=get_name(html)


#异常处理
try:
    for x,y in zip(mp4_url,mp4_name):
        if '|' in y:
            continue
        download(x,y)
except IOError,e:
    print e
