"""hhbg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from game import views
from django.contrib import admin
from django.urls import path
from django.conf import settings

app_name = 'hhbg'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^roll/$', views.roll, name='roll'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^monicker/$', views.monicker, name='monicker')]
#    path('gender/', views.gender, name='gender'),
#    url(r'^end/', include('end.urls')),
#    url(r'^roll/', include('roll.urls')),
#    url(r'^diy/', include('diy.urls')),
#    url(r'^name/', include('name.urls')),
#    url(r'^gender/', include('gender.urls')),
#    path('gender/', views.gender, name='gender'),
