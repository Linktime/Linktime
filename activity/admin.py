from django.contrib import admin
from activity.models import Activity, Team, ActivityTeam, ActivityTag, ActivityTicketType, \
    ActivityOptions, ActivityTicket, ActivityTask

admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(ActivityTag)
admin.site.register(ActivityTeam)
admin.site.register(ActivityTicketType)
admin.site.register(ActivityOptions)
admin.site.register(ActivityTicket)
admin.site.register(ActivityTask)