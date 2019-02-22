"""project URL Configuration

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
from django.urls import path, include
from . import views
from django.conf.urls.static import static# 2 미디어 static 사용
from django.conf import settings
urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<int:blog_id>', views.details, name="details"),
    path('blog/new', views.new, name="new"),
    path('blog/create', views.create, name="create"),
    path('portfolio/', include("portfolio.urls")),
    path('accounts/', include("account.urls")),
    path('newblog/', views.blogpost, name="blogpost"),
    path('error/', views.error, name= "error"),
    path('error2/', views.error2, name="error2"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 3 미디어 쿼리를 사용하기위한 URL
