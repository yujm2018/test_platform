"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login_action', views.login_action),
    path('accounts/login/', views.index),
    path('logout', views.logout),
    path("manage/",include('project_app.urls', namespace="project_app")),
    path("interface/",include('interface_app.urls', namespace="interface_app")),
 ]
