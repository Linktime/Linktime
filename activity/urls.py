from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from activity.views import ActivityListView, ActivityDetailView, ActivityManageDetailView, ActivityParticipantDetailView
from activity.views import activity_create, activity_join, activity_join_cancel, activity_mark, activity_mark_cancel, ajax_activity_update
from activity.models import Activity

urlpatterns = patterns('',
    url(r'^$',ActivityListView.as_view(queryset=Activity.objects.filter(preparing=False).order_by('create_date')),name='activity_list'),
    url(r'^(?P<pk>\d*)/$',ActivityDetailView.as_view(),name='activity_detail'),
    url(r'^create/$',activity_create,name="activity_create"),
    url(r'^(?P<pk>\d*)/join/$',activity_join,name="activity_join"),
    url(r'^(?P<pk>\d*)/cancel_join/$',activity_join_cancel,name="activity_join_cancel"),
    url(r'^(?P<pk>\d*)/mark/$',activity_mark,name="activity_mark"),
    url(r'^(?P<pk>\d*)/cancel_mark/$',activity_mark_cancel,name="activity_mark_cancel"),
    url(r'^(?P<pk>\d*)/manage/$',login_required(ActivityManageDetailView.as_view()),name="activity_manage"),
    url(r'^(?P<pk>\d*)/manage/update/$',ajax_activity_update,name="ajax_activity_update"),
    url(r'^(?P<pk>\d*)/manage/participant$',login_required(ActivityParticipantDetailView.as_view()),name="activity_manage_participant"),
)