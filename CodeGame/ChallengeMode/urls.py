"""
urls.
"""

from django.conf.urls import url
import ChallengeMode.views as views

urlpatterns = [
    url(r'getLevelByUsername$', views.getLevelByUsername),
    url(r'getAllLevels$', views.getAllLevels),
    url(r'getChallengeMapContent$', views.getChallengeMapContent),
    url(r'updateLevelOfUsername$', views.updateLevelOfUsername),
    url(r'addShareLink$', views.addShareLink),
    url(r'getShareLinkById$', views.getShareLinkById),
]
