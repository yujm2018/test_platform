# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 20:04
# @Author  : jimmy
from django.urls import path
from interface_app import views
urlpatterns=[
    path('case_manage',views.case_manage),
    path('api_debug',views.api_debug),
]
app_name = 'interface_app'