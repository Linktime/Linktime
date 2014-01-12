from django.contrib import admin
from activity.models import Activity, Team, ActivityTag

admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(ActivityTag)