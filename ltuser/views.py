# -*- coding:utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.core.urlresolvers import reverse

from ltuser.models import Ltuser, MessageBoard
from activity.models import Team, Activity
from ltuser.forms import RegisterForm, LoginForm

def index(request):
    return render_to_response('index.tpl',context_instance=RequestContext(request))
    #return HttpResponse('Welcome')

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else :
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            ltuser = Ltuser.objects.create(user=user)
            return HttpResponseRedirect(reverse('index'))
        else :
            messages.warning(request,u"您输入的信息不合法，请重新输入")
    return render_to_response('ltuser/register.tpl',{'form':form},context_instance=RequestContext(request))

def ltlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class SingleObjectMixinByUser(SingleObjectMixin):
    """
    验证是否有权限
    """
    def get_object(self):
        object = super(SingleObjectMixinByUser, self).get_object()
        if object.user == self.request.user:
            return object
        else:
            raise Http404

class MultipleObjectMixinByMember(MultipleObjectMixin):
    """
    用于过滤显示自己所在团队
    """
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByMember, self).get_queryset()
        queryset_by_user = queryset.filter(member=self.request.user)
        return queryset_by_user

class MultipleObjectMixinByParticipant(MultipleObjectMixin):
    """
    This mixin filters the queryset in a list-view by request.user
    """
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByParticipant, self).get_queryset()
        queryset_by_user = queryset.filter(participant=self.request.user)
        return queryset_by_user

class UserSpace(DetailView):
    # For other people
    model = Ltuser
    template_name = 'ltuser/user_space.tpl'
    context_object_name = 'ltuser'

class UserInfo(SingleObjectMixinByUser,DetailView):
    # For user himself/herself
    model = Ltuser
    template_name = 'ltuser/user_info.tpl'
    context_object_name = 'ltuser'

class UserTeam(MultipleObjectMixinByMember,ListView):
    model = Team
    template_name = 'ltuser/user_team.tpl'
    context_object_name = 'teams'

class UserActivity(MultipleObjectMixinByParticipant,ListView):
    model = Activity
    template_name = 'ltuser/user_activity.tpl'
    context_object_name = 'activitys'

class UserMessageBoard(ListView):
    model = MessageBoard
    template_name = 'ltuser/user_messageboard'
    context_object_name = 'messageboard'
