#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 10:33 AM
# @Author  : yangqiang
# @File    : urls.py.py
# @Software: PyCharm
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
]