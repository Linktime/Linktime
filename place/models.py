from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lbs(models.Model):
    user = models.ForeignKey(User)
    lat = models.FloatField()
    lng = models.FloatField()
    def __unicode__(self):
        return "%s %f--%f"%(self.user.username,self.lat,self.lng)

class City(models.Model):
    name = models.CharField(max_length=30)
    pid = models.IntegerField()
    lever = models.IntegerField()

    def __unicode__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class UniversityType(models.Model):
    type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.type

class UniversityBelongTo(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class University(models.Model):
    district = models.ForeignKey(Province)
    name = models.CharField(max_length=30)
    type = models.ForeignKey(UniversityType)
    belong_to = models.ForeignKey(UniversityBelongTo)
    def __unicode__(self):
        return self.name