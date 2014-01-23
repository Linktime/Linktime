# -*- coding:utf-8 -*-
from django.db import models
from place.models import City, University, Lbs
from activity.models import Activity, Team

from django.contrib.auth.models import User

# Create your models here.

class Ltuser(models.Model):
    user = models.OneToOneField(User)
    hobby = models.CharField(max_length=30,null=True,blank=True)
    realname = models.CharField(max_length=30,null=True,blank=True)
    location = models.ForeignKey(Lbs,null=True,blank=True)
    university = models.ForeignKey(University,blank=True,null=True)
    city = models.ForeignKey(City,null=True,blank=True)
    auth = models.BooleanField(default=False)
    mark_activity = models.ManyToManyField(Activity,related_name="ltuser_mark_activity",blank=True)
    mark_team = models.ManyToManyField(Team,related_name="ltuser_mark_team",blank=True)

    def __unicode__(self):
        return self.user.username

class Message(models.Model):
    #用户站内信模型
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,related_name='message_sender')
    receiver = models.ForeignKey(User,related_name='message_receiver')
    def __unicode__(self):
        return u'%s回复%s:%s' % (self.sender.alias,self.receiver.alias,self.text)

class MessageBoard(models.Model):
    #留言板模型
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,related_name='message_board_sender')
    receiver = models.ForeignKey(User,related_name="message_board_receiver")
    def __unicode__(self):
        return u'%s回复%s:%s' % (self.sender.alias,self.receiver.alias,self.text)