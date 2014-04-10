# -*- coding:utf-8 -*-

from tastypie.resources import ModelResource, ALL
from tastypie import fields
from tastypie.serializers import Serializer

from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from activity.models import Activity, ActivityTicketType, ActivityTicket

from ltuser.api import UserResource

class OwnerObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(owner=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.owner == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        #return bundle.obj.user == bundle.request.user
        try:
            ActivityTicket.objects.get(owner=bundle.obj.owner,type=bundle.obj.type)
        except:
            return True
        return False

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.owner == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        #raise Unauthorized("Sorry, no deletes.")
        return object_list.filter(owner=bundle.request.user)

    def delete_detail(self, object_list, bundle):
        #raise Unauthorized("Sorry, no deletes.")
        return bundle.obj.owner == bundle.request.user

class ActivityResource(ModelResource):
    ticket_type = fields.ToManyField('activity.api.ActivityTicketTypeResource',"tickettype_activity")
    class Meta:
        queryset = Activity.objects.select_related().filter(preparing=False)
        resource_name = "activity/activity"
        allowed_method = ['get']
        serializer = Serializer(formats=['json',])

class ActivityTicketTypeResource(ModelResource):
    activity = fields.ForeignKey(ActivityResource,'activity')
    class Meta:
        queryset = ActivityTicketType.objects.select_related().filter()
        resource_name = "activity/ticket_type"
        allowed_method = ['get']
        serializer = Serializer(formats=['json',])
        filtering = {
            'activity':ALL,
        }

class ActivityTicketResource(ModelResource):
    owner = fields.ForeignKey(UserResource,'owner')
    type = fields.ForeignKey(ActivityTicketTypeResource,'type')
    class Meta:
        queryset = ActivityTicket.objects.select_related().filter()
        resource_name = "activity/ticket"
        allowed_method = ['get','post','delete']
        serializer = Serializer(formats=['json',])
        authentication = ApiKeyAuthentication()
        authorization = OwnerObjectsOnlyAuthorization()

class ActivityNearbyResource(ModelResource):
    class Meta:
        queryset = Activity.objects.select_related().filter(preparing=False)[:5]
        resource_name = "activity/activity_nearby"
        allowed_method = ['get']
        serializer = Serializer(formats=['json',])

    def hydrate(self, bundle):
        lat = bundle.request.GET.get("lat")
        lng = bundle.request.GET.get("lng")
        # TODO
        return bundle
