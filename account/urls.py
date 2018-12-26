from django.conf.urls import url
from . import views

from django.conf import settings

# 该视图文件中含有login函数
from django.contrib.auth import views as auth_views

urlpatterns = [
   # url(r'^login/$', views.user_login, name="user_login"), #自定义的登录
    url(r'^login/$', auth_views.login, name="user_login"),  #django内置的登录
    url(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"}),
]