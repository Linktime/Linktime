# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import pre_save, pre_delete, post_save
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from activity.models import Activity
from friend.models import Group
from ltuser.models import Message, MessageBoard
# Create your models here.

class Notice(models.Model):
    receiver = models.ForeignKey(User)
    # content_type = models.ForeignKey(ContentType)
    # object_id = models.PositiveIntegerField()
    # content_object = generic.GenericForeignKey('content_type', 'object_id')
    had_read = models.BooleanField(default=False)
    event = models.CharField(max_length=30)
    url = models.URLField(null=True,blank=True)


class ActivityNotice(Notice):
    activity = models.ForeignKey(Activity,null=True,blank=True)
    def __unicode__(self):
        return "%s--activity--%s"%(self.receiver,self.activity)

class ActivityDeleteNotice(Notice):
    creator = models.ForeignKey(User)
    def __unicode__(self):
        return "%s--activity--%s"%(self.receiver,self.creator)

class UserMessageNotice(Notice):
    sender = models.ForeignKey(User)
    def __unicode__(self):
        return "%s--activity--%s"%(self.receiver,self.sender)

class IsAcceptFriendNotice(Notice):
    # event should be friend_accept or friend_refuse
    sender = models.ForeignKey(User)
    def __unicode__(self):
        return "%s--friend--%s"%(self.receiver,self.sender)

class NewFriendNotice(Notice):
    # event should be friend_new
    sender = models.ForeignKey(User)
    accept = models.NullBooleanField(null=True,blank=True)
    group_name = models.CharField(max_length=30)
    def __unicode__(self):
        return "%s--friend--%s"%(self.receiver,self.sender)

    def refuse(self):
        if self.had_read == False:
            self.had_read = True
            self.accept = False
            self.save()
            afn = IsAcceptFriendNotice.objects.create(receiver=self.sender,sender=self.receiver,event=u"friend_refuse")

    def accept(self,receiver_group_name=u"未分组"):
        if self.had_read == False:
            self.accept = True
            self.had_read = True
            self.save()
            sender_group = Group.objects.get(name=self.group_name,owner=self.sender)
            sender_group.member.add(self.receiver)
            receiver_group = Group.objects.get(name=receiver_group_name,owner=self.receiver)
            receiver_group.member.add(self.sender)
            afn = IsAcceptFriendNotice.objects.create(receiver=self.sender,sender=self.receiver,event=u"friend_accept")

def user_message(sender,**kwargs):
    if kwargs['created'] == True:
        message = kwargs['instance']
        #FIXME
        UserMessageNotice.objects.create(receiver=message.receiver,sender=message.sender,event='user_message',url='')

def activity_modify(sender,**kwargs):
    if not kwargs['created'] :
        activity = kwargs['instance']
        for user in activity.participant.all():
            ActivityNotice.objects.create(recevier=user,activity=activity,event="activity_modify",url=reverse('activity_detail',kwargs={'pk':activity.id}))

def activity_delete(sender,**kwargs):
    activity = kwargs['instance']
    for user in activity.participant.all():
        ActivityDeleteNotice.objects.create(recevier=user,creator=activity.creator,event="activity_delete",url=reverse('activity_detail',kwargs={'pk':activity.id}))

post_save.connect(activity_modify,sender=Activity)
pre_delete.connect(activity_delete,sender=Activity)