from django.conf.urls import patterns, include, url

from tastypie.api import Api
from activity.api import ActivityResource, ActivityTicketTypeResource, ActivityTicketResource
from ltuser.api import UserResource

from notice.api import NewFriendNoticeResource

api = Api(api_name="v1")
api.register(ActivityResource())
api.register(ActivityTicketTypeResource())
api.register(ActivityTicketResource())

api.register(UserResource())

api.register(NewFriendNoticeResource())