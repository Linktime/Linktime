from django.conf.urls import patterns, include, url
from activity.views import ActivityListView, ActivityDetailView, ActivityManageDetailView
from activity.views import activity_create, activity_join, activity_join_cancel, activity_mark, activity_mark_cancel
from activity.models import Activity

urlpatterns = patterns('',
    url(r'^$',ActivityListView.as_view(queryset=Activity.objects.filter().order_by('create_date')),name='activity_list'),
    url(r'^(?P<pk>\d*)/$',ActivityDetailView.as_view(),name='activity_detail'),
    url(r'^create/$',activity_create,name="activity_create"),
    url(r'^(?P<pk>\d*)/join/$',activity_join,name="activity_join"),
    url(r'^(?P<pk>\d*)/cancel_join/$',activity_join_cancel,name="activity_join_cancel"),
    url(r'^(?P<pk>\d*)/mark/$',activity_mark,name="activity_mark"),
    url(r'^(?P<pk>\d*)/cancel_mark/$',activity_mark_cancel,name="activity_mark_cancel"),
    url(r'^(?P<pk>\d*)/manage/$',ActivityManageDetailView.as_view(),name="activity_manage"),
)