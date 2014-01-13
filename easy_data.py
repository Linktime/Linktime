# -*- coding:utf-8 -*-
import os
import sys
import datetime

TODAY = datetime.datetime.now()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Linktime.settings")

from django.contrib.auth.models import User
from ltuser.models import Ltuser
from activity.models import Activity, Team

# User
user1 = User.objects.create_user("user1","user1@linktime.cc","123456")
user2 = User.objects.create_user("user2","user2@linktime.cc","123456")
user3 = User.objects.create_user("user3","user3@linktime.cc","123456")

ltuser = Ltuser.objects.create(user=user1)
ltuser = Ltuser.objects.create(user=user2)
ltuser = Ltuser.objects.create(user=user3)

# Activity
activiy1 = Activity.objects.create(creator=user1,date=TODAY.date(),time=TODAY.time(),
                                   place=u"宝山",price=0,name="我是活动哦",introduction="就是来卖萌的")
activiy1.orginizer.add(user1)

activiy2 = Activity.objects.create(creator=user1,date=TODAY.date(),time=TODAY.time(),
                                   place=u"延长",price=0,name="我也是活动哦",introduction="你猜猜看")
activiy2.orginizer.add(user1)

activiy3 = Activity.objects.create(creator=user2,date=TODAY.date(),time=TODAY.time(),
                                   place=u"世纪公园",price=1000,name="大家来找茬",introduction="土豪才能玩的游戏")
activiy3.orginizer.add(user2)

# Team
team1 = Team.objects.create(leader=user1,name="学生会",description="小小生活大社会")
team1.member.add(user1,user2)

team2 = Team.objects.create(leader=user1,name="团委",description="免费洗脑")

team3 = Team.objects.create(leader=user2,name="舞动人生",description="我们只唱歌")
