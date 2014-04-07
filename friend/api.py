# -*- coding:utf-8 -*-

from tastypie.resources import ModelResource,ALL
from tastypie.serializers import Serializer
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization

from friend.models import Group
from ltuser.api import UserResource, SimpleUserResource

class UserObjectsOnlyAuthorization(Authorization):
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
        return True

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.owner == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.owner == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        #raise Unauthorized("Sorry, no deletes.")
        return object_list.filter(owner=bundle.request.user)

    def delete_detail(self, object_list, bundle):
        #raise Unauthorized("Sorry, no deletes.")
        return bundle.obj.owner == bundle.request.user

class GroupResource(ModelResource):
    member = fields.ManyToManyField(SimpleUserResource,'member',full=True)
    class Meta:
        queryset = Group.objects.select_related().filter()
        resource_name = "friend/group"
        allowed_method = ['get',]
        serializer = Serializer(formats=['json',])
        authentication = ApiKeyAuthentication()
        filtering = {
            'name':ALL,
        }