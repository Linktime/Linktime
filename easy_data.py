# -*- coding:utf-8 -*-
import os
import sys
import datetime

TODAY = datetime.datetime.now()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Linktime.settings")

from django.contrib.auth.models import User
from ltuser.models import Ltuser
from activity.models import Activity, Team, GenericMember, GenericOrganizer

# User
user1 = User.objects.create_user(username="user1",email="user1@linktime.cc",password="123456")
user1.set_password("123456")
user1.save()
user2 = User.objects.create_user(username="user2",email="user2@linktime.cc",password="123456")
user2.set_password("123456")
user2.save()
user3 = User.objects.create_user(username="user3",email="user3@linktime.cc",password="123456")
user3.set_password("123456")
user3.save()

ltuser = Ltuser.objects.create(user=user1)
ltuser = Ltuser.objects.create(user=user2)
ltuser = Ltuser.objects.create(user=user3)

# Activity
activiy1 = Activity.objects.create(creator=user1,date=TODAY.date(),time=TODAY.time(),
                                   address=u"宝山",name="我是活动哦",abstract="就是来卖萌的",preparing=False)
generic_object = GenericOrganizer.objects.create(single=user1)
activiy1.organizer.add(generic_object)

activiy2 = Activity.objects.create(creator=user1,date=TODAY.date(),time=TODAY.time(),
                                   address=u"延长",name="我也是活动哦",abstract="你猜猜看",preparing=False)
generic_object = GenericOrganizer.objects.create(single=user1)
activiy2.organizer.add(generic_object)

activiy3 = Activity.objects.create(creator=user2,date=TODAY.date(),time=TODAY.time(),
                                   address=u"世纪公园",name="大家来找茬",abstract="土豪才能玩的游戏",preparing=False)
generic_object = GenericOrganizer.objects.create(single=user2)
activiy3.organizer.add(generic_object)

# Team
team1 = Team.objects.create(leader=user1,name="学生会",description="小小生活大社会")
team1.member.add(user1,user2)

team2 = Team.objects.create(leader=user1,name="团委",description="免费洗脑")

team3 = Team.objects.create(leader=user2,name="舞动人生",description="我们只唱歌")
