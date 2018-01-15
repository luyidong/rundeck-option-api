#!/usr/bin/env python
#coding=utf-8
__author__ = "yidong.lu"
__email__ = "yidongsky@gmail.com"


from django.conf.urls import url

from  .views import (
    list,
    log,
)

urlpatterns = [
    url(r'^list/',list, name='list'),
    url(r'^log',log, name='log'),
]

