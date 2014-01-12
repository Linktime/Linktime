from django.contrib import admin
from ltuser.models import Ltuser, Group, Message, MessageBoard

admin.site.register(Ltuser)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(MessageBoard)