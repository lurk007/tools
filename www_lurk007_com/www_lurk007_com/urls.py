"""www_lurk007_com URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.shortcuts import render, redirect


def home(request):
    """网站主页"""
    context = {
        'gitee_url': 'https://www.gitee.com/lurk007',
        'mail': '758286797@qq.com',
    }
    return render(request, 'blog/Personal-home-page/index.html', context=context)


urlpatterns = [
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls'))
]
