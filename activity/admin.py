from django.contrib import admin
from activity.models import Activity, Team, ActivityTeam, ActivityTag, ActivityPriceType, ActivityOptions, ActivityTicket

admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(ActivityTag)
admin.site.register(ActivityTeam)
admin.site.register(ActivityPriceType)
admin.site.register(ActivityOptions)
admin.site.register(ActivityTicket)