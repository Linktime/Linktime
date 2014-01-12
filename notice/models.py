from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import pre_save, pre_delete, post_save
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from activity.models import Activity
from ltuser.models import Message, MessageBoard
# Create your models here.

class Notice(models.Model):
    receiver = models.ForeignKey(User)
    # content_type = models.ForeignKey(ContentType)
    # object_id = models.PositiveIntegerField()
    # content_object = generic.GenericForeignKey('content_type', 'object_id')
    had_read = models.BooleanField(default=False)
    event = models.CharField(max_length=30)
    url = models.URLField()


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