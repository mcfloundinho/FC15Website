"""
Definition of urls for FC15Website.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
import FC15.views
admin.autodiscover()

urlpatterns = [
    url(r'^$', FC15.views.home, name = 'home'),
    url(r'^home/$', FC15.views.home, name = 'home'),
    url(r'^index/$', FC15.views.index, name = 'index'),
    url(r'^login/$', FC15.views.login, name = 'login'),
    url(r'^logout/$', FC15.views.logout, name = 'logout'),
    url(r'^regist/$', FC15.views.regist, name = 'regist'),
    url(r'^upload/$', FC15.views.upload, name = 'upload'),
    url(r'^postblog/$', FC15.views.postblog, name = 'postblog'),
    url(r'^team/$', FC15.views.team, name = 'team'),
    url(r'^createteam/$', FC15.views.createteam, name = 'createteam'),
    url(r'^resetrequest/$', FC15.views.resetrequest, name = 'resetrequest'),
    url(r'^change/$', FC15.views.change, name = 'change'),
    url(r'^teamdetail/$', FC15.views.teamdetail, name = 'teamdetail'),
    url(r'^teamrequet/$', FC15.views.jointeamrequest, name = 'jointeamrequest'),
    url(r'^quitteam/$', FC15.views.quitteam, name = 'quitteam'),
    url(r'^dismissteam/$', FC15.views.dismissteam, name = 'dismissteam'),

    url(r'^compileall/$', FC15.views.compileall, name = 'compileall'), # test =============================

    url(r'^blogdetail/(?P<pk>[0-9]+)/$', FC15.views.blogdetail, name = 'blogdetail'),
    url(r'^blogedit/(?P<pk>[0-9]+)/$', FC15.views.blogedit, name = 'blogedit'),
    url(r'^blogdelete/(?P<pk>[0-9]+)/$', FC15.views.blogdelete, name = 'blogdelete'),
    url(r'^fileedit/(?P<pk>[0-9]+)/$', FC15.views.fileedit, name = 'fileedit'),
    url(r'^filedelete/(?P<pk>[0-9]+)/$', FC15.views.filedelete, name = 'filedelete'),
    url(r'^filedownload/(?P<pk>[0-9]+)/$', FC15.views.filedownload, name = 'filedownload'),
    url(r'^jointeam/(?P<pk>[0-9]+)/$', FC15.views.jointeam, name = 'jointeam'),
    url(r'^jointeamrequest/(?P<pk>[0-9]+)/$', FC15.views.jointeamrequest, name = 'jointeamrequest'),
    url(r'^mailactivate/(?P<activate_code>.*)/$', FC15.views.activate, name = 'activate'),
    url(r'^resetpassword/(?P<reset_code>.*)/$', FC15.views.resetpassword, name = 'resetpassword'),
    url(r'^acceptrequest/(?P<pk>[0-9]+)/$', FC15.views.acceptrequest, name = 'acceptrequest'),
    url(r'^rejectrequest/(?P<pk>[0-9]+)/$', FC15.views.rejectrequest, name = 'rejectrequest'),

    url(r'^admin/', include(admin.site.urls)),
]
