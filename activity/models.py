#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
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
    # organizer = models.OneToOneField('ActivityOrganizerList',related_name="activity_organizer")
    # participant = models.ManyToManyField('ActivityTicketType',related_name="activity_participant",blank=True)

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

class ActivityTicket(models.Model):
    # 票
    owner = models.ForeignKey(User,related_name='single_ticket_owner')
    type = models.ForeignKey('ActivityTicketType',related_name='single_ticket_type')
    datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s:%s--%s' % (self.owner.username,self.type.type,self.type.activity.name)

class ActivityTeamTicket(models.Model):
    # 票
    owner = models.ForeignKey(ActivityTeam,related_name='teamticket_owner')
    type = models.ForeignKey('ActivityTicketType',related_name='teamticket_type')
    datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s:%s--%s' % (self.owner.username,self.type.type,self.type.activity.name)

class ActivityTicketType(models.Model):
    # 票的种类
    activity = models.ForeignKey(Activity,related_name='tickettype_activity')
    single = models.ManyToManyField(User,related_name='tickettype_single',through=ActivityTicket)
    team = models.ManyToManyField(ActivityTeam,related_name='tickettype_team',through=ActivityTeamTicket)

    type = models.CharField(max_length=20)
    count = models.IntegerField(null=True)
    price = models.IntegerField()

    def __unicode__(self):
        return u'%s:type:%s--price:%s--count:%s' % (self.activity.name,self.type,self.price,self.count)

    def get_ticket_left(self):
        # FIXME
        sale = ActivityTicket.objects.filter(type=self).count()
        return int(self.count) - sale

class ActivitySingleOrganizer(models.Model):
    user = models.ForeignKey(User,related_name='single_organizer_user')
    organizer_list = models.ForeignKey('ActivityOrganizerList',related_name='single_organizer_organizer_list')

class ActivityTeamOrganizer(models.Model):
    team = models.ForeignKey(Team,related_name='team_organizer_team')
    organizer_list = models.ForeignKey('ActivityOrganizerList',related_name='team_organizer_organizer_list')

class ActivityOrganizerList(models.Model):
    activity = models.ForeignKey(Activity,related_name='organizer_list_activity')
    single = models.ManyToManyField(User,related_name='organizer_list_single',through=ActivitySingleOrganizer)
    team = models.ManyToManyField(Team,related_name='organizer_list_team',through=ActivityTeamOrganizer)

class ActivityOptions(models.Model):
    activity = models.OneToOneField(Activity,related_name='activityoptions_activity')
    single_ticket_max = models.IntegerField(null=True)
    team_flag = models.NullBooleanField(null=True,choices=((None,u"组队与个人"),(True,u"组队"),(False,u"个人")))
    team_max = models.IntegerField(null=True)
    during = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s' % (self.activity.name)

class ActivityTag(models.Model):
    activity = models.ForeignKey(Activity,related_name="activitytag_activity")
    category = models.CharField(max_length=30,null=True,blank=True)

class ActivityTask(models.Model):
    activity = models.ForeignKey(Activity,related_name='activitytask_activity')
    assign = models.ManyToManyField(User,related_name='activitytask_assign')
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True)

    def __unicode__(self):
        return u'%s:%s' % (self.activity.name,self.task)

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

def auto_create_options(sender,**kwargs):
    if kwargs['created'] == True:
        activity = kwargs['instance']
        options = ActivityOptions.objects.create(activity=activity)

def auto_create_tickettype(sender,**kwargs):
    if kwargs['created'] == True:
        activity = kwargs['instance']
        ticket_type = ActivityTicketType.objects.create(activity=activity,type=u"门票",price=0)

post_save.connect(auto_create_options,sender=Activity)
post_save.connect(auto_create_tickettype,sender=Activity)