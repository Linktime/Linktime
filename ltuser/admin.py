from django.contrib import admin
from ltuser.models import Ltuser, Message, MessageBoard
from friend.models import Group

from tastypie.models import ApiKey

admin.site.register(Ltuser)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(MessageBoard)
