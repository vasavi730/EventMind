"""Event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from Event.views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'DashBoards',DashViewSet)


urlpatterns = [

    url(r'decline/(?P<id1>[0-9A-Fa-f-]+)$',decline, name='decline'),
    url(r'accept/(?P<id1>[0-9A-Fa-f-]+)/$',accept,name='accept'),
    path('admin/', admin.site.urls),
    path('index/',index),
    path('gallery/',gallery),
    path('about/',about),
    path('wedding/',wedding),
    path('birthday/',birthday),
    path('surprise/',surprise),
    path('product/',product),
    path('theme/',theme),
    path('retirements/',retirements),
    path('annual/',annual),
    path('booking/',booking),
    path('update/',update),
    path('accepted/',accepted),
    path('query_list/',query_list),
    path('rejected/',rejected),
    path('accepted_list/',accepted_list),
    path('rejected_list/',rejected_list),
    path('login/',login),
    path('recieved/',received),
    path('contact/',contact),
    path('admin_login/',admin_login),
    path('StatusBoard/',StatusBoard),
    path('pending/',pending),
    path('pending_list/',pending_list),
    path('pending_list/<uuid:client_id>',pending_list),
    path('',include(router.urls)),
    path('about/',about),
    path('query/',query),
    path('confirm/',confirm),
    path('api-auth/',include('rest_framework.urls',
        namespace='rest_framework'))

]