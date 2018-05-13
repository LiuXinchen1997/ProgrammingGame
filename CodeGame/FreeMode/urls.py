"""
urls.
"""

from django.conf.urls import url
from django.contrib import admin
import FreeMode.views as views

urlpatterns = [
    url(r'test$', views.test),
    url(r'getAllCreatedMapByUsername$', views.getAllCreatedMapByUsername),
    url(r'getAllReleasedMapByUsername$', views.getAllReleasedMapByUsername),
    url(r'getAllCollectedMapByUsername$', views.getAllCollectedMapByUsername),
    url(r'getAllReleasedMap$', views.getAllReleasedMap),
    url(r'deleteMapById$', views.deleteMapById),
    url(r'setLikeById$', views.setLikeById),
    url(r'cancelLikeById$', views.cancelLikeById),
    url(r'setCollectById$', views.setCollectById),
    url(r'cancelCollectById$', views.cancelCollectById),
    url(r'saveCreateMap$', views.saveCreateMap),
    url(r'getFreeMapContent$', views.getFreeMapContent),
    url(r'updateFreeMapContent$', views.updateFreeMapContent),
    url(r'uploadFreeMapById$', views.uploadFreeMapById),
]
