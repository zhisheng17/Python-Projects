## 图片爬虫
- 爬取极客学院首页的图片并下载下来
- 碰到的问题：
	+ ``import requests``导入报错,报错信息：``ImportError: No module named 'requests'``
	
	+ 报错解决方法：[ImportError: No module named 'requests'](http://my.oschina.net/chier/blog/341419)
	
	+ 就是代码中不能含有中文，否则报错**  “ UnicodeDecodeError: ‘gbk’ codec can’t decode bytes in position 2-3: illegal multibyte sequ ” **
	
	+ 报错解决方案：[Python中遇到"UnicodeDecodeError: ‘gbk’ codec can’t decode bytes in position 2-3: illegal multibyte sequ](http://blog.csdn.net/tzs_1041218129/article/details/51581170)
	
	+ 发现极客学院部分图片不能爬取