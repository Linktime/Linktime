from django.conf.urls import patterns, include, url
from ltuser.views import UserInfo, UserTeam
from django.contrib.auth.decorators import login_required
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^(?P<pk>\d*)/info/$',login_required(UserInfo.as_view()),name='user_info'),
    url(r'^(?P<pk>\d*)/team/$',login_required(UserTeam.as_view()),name="user_team"),
)
