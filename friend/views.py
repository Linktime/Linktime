# -*- coding:utf-8 -*-
# Create your views here.

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from friend.models import Group
from notice.models import NewFriendNotice, IsAcceptFriendNotice

class SingleObjectMixinByOwner(SingleObjectMixin):
    def get_object(self):
        object = super(SingleObjectMixinByOwner, self).get_object()
        if object.owner == self.request.user:
            return object
        else:
            raise Http404

class MultipleObjectMixinByOwner(MultipleObjectMixin):
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByOwner, self).get_queryset()
        queryset_by_user = queryset.filter(owner=self.request.user)
        return queryset_by_user

class GroupListView(ListView,MultipleObjectMixinByOwner):
    model = Group
    template_name = 'friend/friend_list.tpl'
    context_object_name = 'groups'

class GroupDetailView(DetailView,SingleObjectMixinByOwner):
    model = Group
    template_name = 'friend/friend_detail.tpl'
    context_object_name = 'group'

@login_required
def search_friend(request):
    return render_to_response("friend/friend_search.tpl",context_instance=RequestContext(request))

# @csrf_exempt
def ajax_search_friend(request):
    username = request.POST.get("username")
    if username:
        users = User.objects.filter(username__contains=username)
        count = len(users)
    else :
        users = None
        count = 0
    return render_to_response("friend/ajax_friend_list.tpl",{"users":users,"count":count},context_instance=RequestContext(request))

def ajax_group_list(request):
    groups = Group.objects.filter(owner=request.user)
    count = len(groups)
    return render_to_response("friend/ajax_group_list.tpl",{"groups":groups,"count":count},context_instance=RequestContext(request))

@login_required
def friend_add_pre(request):
    user_id = request.POST.get("user_id")
    group_name = request.POST.get("group_name",u"未分组")
    try :
        friend = User.objects.get(id=int(user_id))
        nfn = NewFriendNotice.objects.create(receiver=friend,sender=request.user,event="friend_new",group_name=group_name)
        messages.info(request,u"已向用户发送好友申请")
    except :
        messages.warning(request,u"未找到您要添加的好友")
    return HttpResponseRedirect(reverse("group_list"))

@login_required
def friend_add_accept(request):
    notice_id = request.POST.get("notice_id")
    group_name = request.POST.get("group_name")
    nfn = NewFriendNotice.objects.get(id=int(notice_id))
    nfn.accept(group_name)
    messages.info(request,u"您与%s已成为好友"%nfn.sender.username)
    return HttpResponseRedirect(reverse("group_list"))

@login_required
def friend_add_refuse(request):
    notice_id = request.POST.get("notice_id")
    group_name = request.POST.get("group_name")
    nfn = NewFriendNotice.objects.get(id=int(notice_id))
    nfn.refuse()
    return HttpResponseRedirect(reverse("group_list"))

@login_required
def friend_remove(request):
    user_id = request.POST.get("user_id")
    friend = User.objects.get(id=int(user_id))
    group_name = request.POST.get("group_name",u"未分组")
    group = Group.objects.get(name=group_name)
    group.member.remove(friend)
    messages.info(request,u"您与%s已解除好友关系"%friend.username)
    return HttpResponseRedirect(reverse("group_detail",kwargs={"pk":group.id}))

