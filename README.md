# scanner
漏扫详细说明文档

一：目录结构说明

   scanner：
topmgr.py : 后台service，负责扫描任务的管理工作
topscan.py: 扫描流程的入口程序
lib: 漏扫流程代码
scripts: 规则脚本目录
   topweb：前台界面

二：使用的库介绍

  注意：下面的版本是我使用的版本，不代表必须

  后台：
python2.76   建议使用Python2高版本
django1.6.1  Python的web框架
gevent1.0    Python的高性能网络库，需要安装greenlet
mysqldb     后台数据库我使用的是mysql
pywin32     使用了windows中的services，所以需pywin32包
beautifulsoup4 爬虫使用了bs4
requests      比较好用的http请求包(不需要安装，在thirdparty目录下)

  前台使用库介绍：
  	bootstrap    界面总体是用的bootstrap v3
  	jquery/jstree  树形控件使用的是jstree

三：数据库说明

   手动新建新数据库，默认kehan
   可通过django新建所有的表，python manage.py syncdb

   表介绍：
   		task表：任务表
        	base字段: 主要用来处理同域名不同站点问题，如起始url为								  http://betteryinzhixin.com/vul/vul.php，如果设置base为/vul/，就只会扫					  描/vul/目录
progress字段：用来实现扫描进度，每开始扫描规则，将添加规则id，结束添				 加end

url表: 爬虫url表
result表: 扫描结果表
rule表：规则表
priority: 优先级1-10，越小越先检测
