# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Group(models.Model):
    #用户好友分组模型
    name = models.CharField(max_length=30)
    member = models.ManyToManyField(User,related_name="group_member")
    owner = models.ForeignKey(User,related_name="group_owner")
    def __unicode__(self):
        return u'%s的好友分组：%s' % (self.owner.username,self.name)

def default_group(sender,**kwargs):
    # import code;code.interact(local=locals())
    if kwargs['created']==True:
        instance = kwargs["instance"]
        group = Group.objects.create(name=u"未分组",owner=instance)

post_save.connect(default_group,sender=User)