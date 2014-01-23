#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from place.models import GenericPlace, Lbs

# Create your models here.
#以下为与活动相关的数据模型

class Team(models.Model):
    #某某神秘组织
    name = models.CharField(max_length=30,unique=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True) #用以记录小组创办时间
    leader = models.ForeignKey(User,related_name="team_leader")
    member = models.ManyToManyField(User,related_name="team_member")

    def set_logo(self):
        pass

    def get_logo(self):
        pass

    def __unicode__(self):
        return self.name

class ActivityTeam(Team):
    # 活动分组
    pass

class GenericMember(models.Model):
    # content_type = models.ForeignKey(ContentType)
    # object_id = models.PositiveIntegerField()
    # content_object = generic.GenericForeignKey('content_type', 'object_id')
    single = models.ForeignKey(User,related_name="genericmember_single",null=True)
    team = models.ForeignKey(ActivityTeam,related_name="genericmember_team",null=True)
    team_flag = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)

    def get_name(self):
        if self.team_flag :
            return self.team.name
        else :
            return self.single.username

class GenericOrganizer(models.Model):
    single = models.ForeignKey(User,related_name="genericorganizer_single",null=True)
    team = models.ForeignKey(ActivityTeam,related_name="genericorganizer_team",null=True)
    team_flag = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=10,default="1")
    
    def get_name(self):
        if self.team_flag :
            return self.team.name
        else :
            return self.single.username


class Activity(models.Model):
    #活动模型
    name = models.CharField(max_length=30)
    abstract = models.CharField(max_length=200)
    introduction = models.TextField(default=u"暂无详情介绍")
    date = models.DateField() #活动举办时间，应为DateTime类型，待改
    time = models.TimeField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(GenericPlace,related_name='activity_palce',blank=True,null=True)
    address = models.CharField(max_length=30)
    preparing = models.BooleanField(default=True)
    lbs = models.OneToOneField(Lbs,null=True,blank=True)
    creator = models.ForeignKey(User,related_name='activity_creator')
    organizer = models.ManyToManyField(GenericOrganizer,related_name="activity_organizer")
    sponsor = models.ManyToManyField(GenericOrganizer,related_name="activity_sponsor",blank=True)
    participant = models.ManyToManyField(GenericMember,related_name="activity_participant",blank=True)

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

class ActivityPriceType(models.Model):
    # 票的种类
    activity = models.ForeignKey(Activity)
    type = models.CharField(max_length=20)
    count = models.IntegerField()
    price = models.IntegerField()

    def __unicode__(self):
        return u'%s:type:%s--price:%s--count:%s' % (self.activity.name,self.type,self.price,self.count)

class ActivityTicket(models.Model):
    # 票
    owner = models.ForeignKey(GenericMember,related_name='activityticket_owner')
    type = models.ForeignKey(ActivityPriceType,related_name='activityticket_type')

    def __unicode__(self):
        return u'%s:%s--%s' % (self.owner.username,self.type.type,self.type.activity.name)

class ActivityOptions(models.Model):
    activity = models.OneToOneField(Activity,related_name='activityoptions_activity')
    team_flag = models.NullBooleanField(null=True)
    team_max = models.IntegerField()
    during = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s' % (self.activity.name)

class ActivityTag(models.Model):
    activity = models.ForeignKey(Activity,related_name="activitytag_activity")
    category = models.CharField(max_length=30,null=True,blank=True)

class ActivityIntroduction(models.Model):
    activity = models.ForeignKey(Activity)
    # content_type = models.ForeignKey(ContentType)
    # object_id = models.PositiveIntegerField()
    # content_object = generic.GenericForeignKey('content_type', 'object_id')
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