# coding:utf-8
# @Time    :  2020-06-23 16:27
# @Author  : Administrator
# @File    : learning_log
# @Description :
from django.conf.urls import url
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    # 主页
    # url(r'^$', views.index, name='index'),
    # path('',views.index),
    re_path('^$', views.index, name='index'),
    # 显示所有披萨
    path('pizza/', views.pizzas,name='pizzas'),
    # 披萨的配料
    url(r'^pizza/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
]

app_name = 'pizzas'
