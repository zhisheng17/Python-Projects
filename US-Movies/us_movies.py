#-*-coding:utf8-*-
#created by 10412

import requests
import re
import sys
import threading
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class Archives(object):

    #保存下载链接函数
    def save_links(self, url):
        try:
            data = requests.get(url, timeout = 3)
            content = data.text
            #正则表达式匹配下载链接
            link_pat = '"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"'
            #获取电视剧名称
            name_pat = re.compile(r'<h2 class="entry_title">(.*?)</h2>', re.S)

            links = set(re.findall(link_pat, content))
            name = re.findall(name_pat, content)
            links_dict = {}
            count = len(links)
        except Exception,e:
            pass
        for i in links:
            links_dict[int(i[1][1:3]) * 100 + int(i[2][1:3])] = i   #把剧集按s和e提取编号
        try:
            with open(name[0].replace('/',' ')+'.txt','w') as f:
                print name[0]
                for i in sorted(list(links_dict.keys())):   #按季数+集数排序顺序写入
                    f.write(links_dict[i][0] + '\n')
            print "Get links ... ", name[0], count
        except Exception,e:
            pass

    #获取电影文章的 URL 函数
    def get_urls(self):
        try:
            for i in range(2015,25000):
                base_url = 'http://cn163.net/archives/'
                url = base_url+str(i)+'/'
                if requests.get(url).status_code == 404:    #status_code判断请求返回的状态，只要是返回状态码是404的我们都把它跳过，其他的都进去爬取链接，这就解决了url不存在的问题了
                    continue
                else:
                    self.save_links(url)    #调用保存下载链接函数
        except Exception,e:
            pass

    def main(self):
        thread1 = threading.Thread(target = self.get_urls())
        thread1.start()
        thread1.join()

if __name__ == '__main__':
    start = time.time()
    a = Archives()
    a.main()
    end = time.time()
    print end - start