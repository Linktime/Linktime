#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.
#以下为与活动相关的数据模型

class Team(models.Model):
    #某某神秘组织
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField(auto_now_add=True) #用以记录小组创办时间
    leader = models.ForeignKey(User,related_name="team_leader")
    member = models.ManyToManyField(User,related_name="team_member")
    def __unicode__(self):
        return self.name

class UserOrTeam(models.Model):
    user = models.ForeignKey(User,null=True)
    team = models.ForeignKey(Team,null=True)
    user_or_team = models.BooleanField(default=False)

    def get(self):
        if self.user_or_team==False:
            return self.user
        else :
            return self.team

class Activity(models.Model):
    #活动模型
    name = models.CharField(max_length=30)
    introduction = models.TextField()
    date = models.DateField() #活动举办时间，应为DateTime类型，待改
    create_date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.CharField(max_length=30,null=True,blank=True)
    # tag = models.ForeignKey('ActivityTag',null=True,blank=True)
    #FIXME The follow field should allow add as a group
    creator = models.ForeignKey(User,related_name='activity_creater')
    organizer = models.ManyToManyField(User,related_name="activity_organizer")
    sponsor = models.ManyToManyField(User,related_name="activity_sponsor",null=True,blank=True)
    participant = models.ManyToManyField(User,related_name="activity_participant",null=True,blank=True)

    def __unicode__(self):
        return u"%s" % self.name

class Comment(models.Model):
    #活动中用户的评论模型
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey('Activity',related_name='comment_activity')
    owner = models.ForeignKey(User,related_name='comment_owner')
    at = models.ManyToManyField(User,related_name='comment_at')
    def __unicode__(self):
        return u'%s:%s,Time:%s' % (self.owner.alias,self.text,self.date)


class ActivityTag(models.Model):
    category = models.CharField(max_length=30,null=True,blank=True)

class ActivityIntroduction(models.Model):
    activity = models.ForeignKey(Activity)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    type = models.CharField(max_length=30)

class VideoIntroduction(ActivityIntroduction):
    video_web = models.CharField(max_length=20)
    video_id = models.CharField(max_length=100)
    video_title = models.CharField(max_length=20)

class TextIntroduction(ActivityIntroduction):
    text_content = models.CharField(max_length=200)

class ImageIntroduction(ActivityIntroduction):
    image_title = models.CharField(max_length=20)
    image_url = models.URLField()

    def getUrl(self):
        pass