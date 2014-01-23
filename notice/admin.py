from django.contrib import admin
from notice.models import ActivityNotice

from notice.models import NewFriendNotice
from notice.models import IsAcceptFriendNotice

admin.site.register(ActivityNotice)
admin.site.register(NewFriendNotice)
admin.site.register(IsAcceptFriendNotice)
