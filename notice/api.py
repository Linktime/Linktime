from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from django.db.models import Q

from ltuser.api import UserResource

from notice.models import NewFriendNotice

class SenderObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(sender=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.sender == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        #return bundle.obj.user == bundle.request.user
        try:
            NewFriendNotice.objects.get(sender=bundle.obj.sender,receiver=bundle.obj.receiver,had_read=False)
        except:
            return True
        return False

    def update_list(self, object_list, bundle):
        allowed = []
        return allowed

    def update_detail(self, object_list, bundle):
        return False

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        #raise Unauthorized("Sorry, no deletes.")
        return object_list.filter(sender=bundle.request.user)

    def delete_detail(self, object_list, bundle):
        #raise Unauthorized("Sorry, no deletes.")
        return bundle.obj.sender == bundle.request.user

class ReceiverObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(receiver=bundle.request.user,had_read=False)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.receiver == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        return False

    def update_list(self, object_list, bundle):
        allowed = []
        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.receiver == bundle.request.user:
                allowed.append(obj)
        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.receiver == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        #raise Unauthorized("Sorry, no deletes.")
        return object_list.filter(sender=bundle.request.user)

    def delete_detail(self, object_list, bundle):
        #raise Unauthorized("Sorry, no deletes.")
        return bundle.obj.sender == bundle.request.user

class NewFriendNoticeResource(ModelResource):
    sender = fields.ForeignKey(UserResource,'sender')
    receiver = fields.ForeignKey(UserResource,'receiver')
    class Meta:
        queryset = NewFriendNotice.objects.select_related().filter()
        resource_name = "notice/new_friend_notice"
        allowed_method = ['get','post',]
        serializer = Serializer(formats=['json',])
        authentication = ApiKeyAuthentication()
        authorization = SenderObjectsOnlyAuthorization()

class AcceptFriendNoticeResource(ModelResource):
    sender = fields.ForeignKey(UserResource,'sender')
    receiver = fields.ForeignKey(UserResource,'receiver')
    class Meta:
        queryset = NewFriendNotice.objects.select_related().filter()
        resource_name = "notice/accept_friend_notice"
        allowed_method = ['get','put',]
        serializer = Serializer(formats=['json',])
        authentication = ApiKeyAuthentication()
        authorization = ReceiverObjectsOnlyAuthorization()

    def full_hydrate(self, bundle):
        import code;code.interact(local=locals())
        accept = bundle.data.get("accept")
        group_name = bundle.data.get("group")
        if accept:
            bundle.obj.accept(group_name)
        return bundle