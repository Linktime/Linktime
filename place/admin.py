from django.contrib import admin
from place.models import City, Region, Province, GenericPlace, Lbs
from place.models import University, UniversityBelongTo, UniversityType

admin.site.register(City)
admin.site.register(Region)
admin.site.register(Province)
admin.site.register(GenericPlace)
admin.site.register(Lbs)
admin.site.register(University)
admin.site.register(UniversityBelongTo)
admin.site.register(UniversityType)
