# coding:utf-8
# @Time    :  2020-06-22 18:20
# @Author  : Administrator
# @File    : learning_log
# @Description : 
"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
]