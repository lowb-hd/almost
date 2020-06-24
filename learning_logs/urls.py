# coding:utf-8
# @Time    :  2020-06-22 18:20
# @Author  : Administrator
# @File    : learning_log
# @Description : 
"""定义learning_logs的URL模式"""
from django.conf.urls import url
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    # 主页
    # url(r'^$', views.index, name='index'),
    # path('',views.index),
    re_path('^$', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics,name='topics'),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]

app_name = 'learning_logs'