# Python-Spiders
some projects of Python-Spider during my study Python

1. Picture-download-jikexueyuan

2. Picture-Spider-tieba

3. 糗事百科段子爬取

    + **Spider1-qiushibaike.py**：爬取糗事百科的8小时最新页的段子。包含的信息有作者名称，觉得好笑人数，评论人数，发布的内容。如果发布的内容中含有图片的话，则过滤图片，内容依然显示出来。

    + **Spider2-qiushibaike.py**：在Spider1-qiushibaike.py基础上，引入类和方法，进行优化和封装，爬取糗事百科的24小时热门页的段子。进一步优化，每按一次回车更新一条内容，当前页的内容抓取完毕后，自动抓取下一页的内容，按‘q’退出。

    + **Spider3-qiushibaike.py**：在Spiders-qiushibaike.py基础上，爬取了百科段子的评论。按C查看当前这个糗事的评论，当切换到查看评论时，换回车显示下一个评论,按Q退出回到查看糗事。糗事段子页数是一页一页加载的，如果你已经看完所有的糗事，就会自动退出！