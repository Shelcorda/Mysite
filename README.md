# Mysite
跟着老齐学python——django，代码包括了第1章、第2章、第3章、第4章、第7章
1. 第1章，简单的设置，了解django属于MVT模式，即Model，View，Template，了解三者之间的调用关系（blog）
2. 第2章，用户管理（account）
   - 使用自定义的方法设置登录，此外可以设置好看的登录模板
   - 使用Django自带的login函数，在auth视图中有定义好的login函数，其模板的名字为"registration/login.html"；或者也可以指定模板：url(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"})
   - 使用Django自带的user.is_authenticated判断用户是否处于登录状态
   - 使用Django自带的logout函数，进行退出操作，同login函数
   - 使用自定义的方法设置注册，可以直接使用User模型中自带的属性，不需要另外建Model；当需要User中不存在的属性时，也可以拓展User模型
   - 使用Django自带的密码重置和修改函数，进行有关密码的修改和重置
   - 个人信息的设置
3. 第3章，文章管理（article）
   - 栏目的设置，实现栏目的添加、编辑、删除功能
   - 文章的设置，实现文章的增删改查功能，并对文章列表进行分页处理
   - 读者也可以查看文章
4. 第4章，拓展网站功能（article）
   - 增加了点赞功能
   - 增加了标签功能，可以进行归类
5. 第7章，创建在线学习使用
   - 主要是学习类视图
   - 在类视图的基础上增加了课程发布、报名课程等功能
