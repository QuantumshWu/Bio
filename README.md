# Bio
这是一个基于django框架，前端使用bootstrap,数据库使用mysql的小型网站。<br> 
网站包含主页，搜索页面，数据显示页面和管理页面等。对于匿名用户，可以利用正则表达式查找数据库中的对应基因。而对于拥有账号的用户，可以修改和添加搜索<br> 
标签，修改和添加基因数据等。对于管理员用户，可以修改和添加账号。<br> 
<br> 
bio_website是django目录<br> 
----bio_website是基本的设置，重要的设置包括基本路径和数据库配置都在setting.py中<br> 
----data是主文件<br> 
--------templates是页面html模板，通过views.py连接数据库进行渲染。<br> 
--------models.py是数据库模型<br> 
--------urls.py是url到视图函数views.py的映射关系<br> 
--------views.py是视图函数，定义了每个url对应的处理函数。<br> 
--------static是静态文件，包含js库和一些图片以及字体<br> 
--------migrations是数据库的日志<br> 
----static另外一些静态文件<br> 
<br> 
    
    
bio_database包含了运行需要的python库,包括django等，具体项目在pip-requi.txt。<br> 
<br> 



对于linux用户，clone下来之后，首先配置mysql.<br> 
用create database XXXXX character set utf8;建库，保证和setting中的账号密码库名对应就行。<br> 
之后运行根目录下的syncdb.sh同步数据库。<br> 
之后运行test.sh在本机运行本网站。bio_database已经包含了本网站所需要的python库，test.sh会将当前环境<br> 
切换到bio_database中。对于希望在公网上运行网站的用户，还需要额外配置apache等服务器，利用WSGI可以实现apache与dajngo的结合。<br> 
