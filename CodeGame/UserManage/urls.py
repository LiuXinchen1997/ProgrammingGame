"""
urls.
"""

from django.conf.urls import url
import UserManage.views as views

urlpatterns = [
    url(r'getDemo$', views.getDemo),
    url(r'postDemo$', views.postDemo),
    url(r'sendMessage$', views.sendMessage),
    url(r'checkTelNum$', views.telNumExists),
    url(r'register$', views.register),
    url(r'UpdatePsw$', views.UpdatePsw),
    url(r'UpdatePsdByTelNum', views.UpdatePsdByTelNum),
    url(r'Login$', views.Login),
    url(r'member$', views.member),
    url(r'getByUsername$', views.getByUsername),
    url(r'modifyInfo$', views.modifyInfo),
    url(r'checkPassword$', views.checkPassword),
    url(r'getUsernameByTel$', views.getUsernameByTel),
    url(r'getMemberByUsername$', views.getMemberByUsername),
]
