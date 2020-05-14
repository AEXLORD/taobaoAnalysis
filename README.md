# taobaoAnalysis
一个不成熟的半自动淘宝商品评论爬取、清洗、分析、生成报表工具

---

## 我需要什么？

    1.configparser
    2.snownlp
    3.xlwt
    4.xlrd
    5.matplotlib
    6.collections
    7.requests

---

## 我要怎么运行？

为了更方便直观的看，我自己制作了一个[使用视频](https://www.bilibili.com/video/BV1CK41157h7)在bilibili上可观看

同时，直接打开配置文件`Infor.conf`并按照如下编写也可以运行项目:

    [taobao]
    name=
    pageNumber=
    url=
    Cookie=
    referer=

其中，`name`可以随意填写，目的是给你这次要爬取的东西起个名字，`pageNumber`则是你想要爬取的篇评论页数，`url`不是网页的url，而是评论区的url
需要你通过在网页端打开开发者工具，找到一个叫做"list"的文件，复制它的地址，`Cookie`十分关键，淘宝反爬严格，此方法也是建立在模拟浏览器的方法获取信息的，所以这个一定要有。获取方法也是在开发者工具中“headers”查找，`referer`同样也在“headers”中查找

---

## 结语

如有任何问题，请留言至`issues`中，我会在看到后回复，或者发邮件到我的邮箱中，609924504zyz@gmail.com
  
