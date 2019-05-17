# test
天天生鲜项目
项目开发环境：pycharm，python3.6，window10
运行环境：centos7.2
依赖文件requesments.txt
天天生鲜是一个B2C的网络电商应用，依托于网络的便捷性，可以针对定点区域进行快速的配送货物，该应用接入了支付宝支付功能和方便管理人员管理的Xadmin后台。使用FastDFS存储图片等类型的文件来减轻服务器存储压力，使用Celery去异步处理邮件发送等耗时问题，使用Nginx管理静态资源

主要功能包括：注册登录 | 用户中心 | 商品信息 | 购物车 | 订单模块
技术实现：Mysql, Redis, FastDFS, Celery, Nginx+uwsgi, Django2.0+Xadmin

Attention:
  原项目使用django1.9+admin
  可以更新为django2.0 更改所有的路由urls.py模块即可 使用re_path 去替换 url（from django.urls import include,re_path）
  xadmin 可以使用pip安装 依赖模块有 crispy_forms
  配置xadmin, crispy_forms添加到  settings.py INSTALLED_APPS应用列表
  在主urls.py文件添加
      url(r'^xadmin/', xadmin.site.urls),
  
  在每个app目录下添加adminx.py文件在这里注册你的model 和admin类似；xadmin会自动读取该模块
  然后重新生成migrations all并migrate同步数据库即可
  
