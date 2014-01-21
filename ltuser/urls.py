from django.conf.urls import patterns, include, url
from ltuser.views import UserInfo, UserTeam, UserParticipantActivity, UserSpace, UserTrends, UserOrganizerActivity, UserCreatorActivity
from ltuser.views import UserActivity, UserSponsorActivity, UserMarkerActivity
from activity.models import Activity
from django.contrib.auth.decorators import login_required
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/space/$',UserSpace.as_view(),name="user_space"),
    url(r'^(?P<pk>\d+)/info/$',login_required(UserInfo.as_view()),name='user_info'),
    url(r'^(?P<pk>\d+)/trends/$',login_required(UserTrends.as_view()),name='user_trends'),
    url(r'^(?P<pk>\d+)/team/$',login_required(UserTeam.as_view()),name="user_team"),
    url(r'(?P<pk>\d+)/activity/$',login_required(UserActivity.as_view()),name="user_activity"),
    url(r'(?P<pk>\d+)/activity/participant/$',login_required(UserParticipantActivity.as_view(queryset=Activity.objects.filter().order_by('create_date'))),name="user_activity_participant"),
    url(r'(?P<pk>\d+)/activity/organizer/$',login_required(UserOrganizerActivity.as_view(queryset=Activity.objects.filter().order_by('create_date'))),name="user_activity_organizer"),
    url(r'(?P<pk>\d+)/activity/creator/$',login_required(UserCreatorActivity.as_view(queryset=Activity.objects.filter().order_by('create_date'))),name="user_activity_creator"),
    url(r'(?P<pk>\d+)/activity/sponsor/$',login_required(UserSponsorActivity.as_view(queryset=Activity.objects.filter().order_by('create_date'))),name="user_activity_sponsor"),
    url(r'(?P<pk>\d+)/activity/marker/$',login_required(UserMarkerActivity.as_view(queryset=Activity.objects.filter().order_by('create_date'))),name="user_activity_marker"),
)
