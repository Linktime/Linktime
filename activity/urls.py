from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from activity.views import ActivityListView, ActivityDetailView, ActivityManageDetailView, \
    ActivityParticipantDetailView, ActivityOptionsDetailView,ActivityTaskDetailView, ActivityStatisticsDetailView, \
    ActivityQrCodeView, ActivitySearchListView, ActivitySearchMapListView
from activity.views import activity_create, activity_single_join, activity_single_join_cancel, activity_mark, activity_mark_cancel, ajax_activity_update
from activity.views import activity_release
from activity.models import Activity

from activity.views import activity_qrcode,mobile_activity_nearby

urlpatterns = patterns('',
    url(r'^$',ActivityListView.as_view(queryset=Activity.objects.filter(preparing=False).order_by('create_date')),name='activity_list'),
    url(r'^(?P<pk>\d*)/$',ActivityDetailView.as_view(),name='activity_detail'),
    url(r'^create/$',activity_create,name="activity_create"),
    url(r'^search/$',ActivitySearchListView.as_view(queryset=Activity.objects.filter(preparing=False)),name="activity_search"),
    url(r'^search_map/$',ActivitySearchMapListView.as_view(queryset=Activity.objects.filter(preparing=False)),name="activity_search_map"),
    url(r'^(?P<pk>\d*)/qrcode/$',login_required(ActivityQrCodeView.as_view()),name="activity_qrcode"),
    url(r'^(?P<pk>\d*)/single_join/$',activity_single_join,name="activity_single_join"),
    url(r'^(?P<pk>\d*)/single_cancel_join/$',activity_single_join_cancel,name="activity_single_join_cancel"),
    url(r'^(?P<pk>\d*)/mark/$',activity_mark,name="activity_mark"),
    url(r'^(?P<pk>\d*)/cancel_mark/$',activity_mark_cancel,name="activity_mark_cancel"),
    url(r'^(?P<pk>\d*)/manage/$',login_required(ActivityManageDetailView.as_view()),name="activity_manage"),
    url(r'^(?P<pk>\d*)/manage/options/$',login_required(ActivityOptionsDetailView.as_view()),name="activity_manage_options"),
    url(r'^(?P<pk>\d*)/manage/task/$',login_required(ActivityTaskDetailView.as_view()),name="activity_manage_task"),
    url(r'^(?P<pk>\d*)/manage/release/$',activity_release,name="activity_release"),
    url(r'^(?P<pk>\d*)/manage/update/$',ajax_activity_update,name="ajax_activity_update"),
    url(r'^(?P<pk>\d*)/manage/participant/$',login_required(ActivityParticipantDetailView.as_view()),name="activity_manage_participant"),
    url(r'^(?P<pk>\d*)/manage/statistics/$',login_required(ActivityStatisticsDetailView.as_view()),name="activity_manage_statistics"),

    url(r'^(?P<pk>\d*)/qrcode_img/$',activity_qrcode,name="activity_qrcode_img"),
    url(r'^mobile_activity_nearby/$',mobile_activity_nearby),
)