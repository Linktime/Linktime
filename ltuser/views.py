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
from django.db.models import Q

from ltuser.models import Ltuser, MessageBoard
from activity.models import Team, Activity
from ltuser.forms import RegisterForm, LoginForm
from friend.models import Group

def index(request):
    return render_to_response('index.tpl',context_instance=RequestContext(request))
    #return HttpResponse('Welcome')

def test(request):
    return render_to_response('test.tpl',context_instance=RequestContext(request))

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

class MultipleObjectMixinByOwner(MultipleObjectMixin):
    """
    用于过滤显示自己的好友圈
    """
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByOwner, self).get_queryset()
        queryset_by_user = queryset.filter(owner=self.request.user)
        return queryset_by_user

class MultipleObjectMixinByParticipant(MultipleObjectMixin):
    """
    This mixin filters the queryset in a list-view by request.user
    """
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByParticipant, self).get_queryset()
        queryset_by_user = queryset.filter(Q(tickettype_activity__single=self.request.user)|Q(tickettype_activity__team__member=self.request.user))
        return queryset_by_user

class MultipleObjectMixinByOrganizer(MultipleObjectMixin):
    """
    This mixin filters the queryset in a list-view by request.user
    """
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByOrganizer, self).get_queryset()
        queryset_by_user = queryset.filter(Q(organizer_list_activity__single=self.request.user)|Q(organizer_list_activity__team__member=self.request.user))
        return queryset_by_user

class MultipleObjectMixinByCreator(MultipleObjectMixin):
    """
    This mixin filters the queryset in a list-view by request.user
    """
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByCreator, self).get_queryset()
        queryset_by_user = queryset.filter(creator=self.request.user)
        return queryset_by_user

class MultipleObjectMixinByMarkActivity(MultipleObjectMixin):
    """
    This mixin filters the queryset in a list-view by request.user
    """
    def get_queryset(self):
        # queryset = super(MultipleObjectMixinByMarkActivity, self).get_queryset()
        queryset_by_user = self.request.user.ltuser.mark_activity.filter()
        return queryset_by_user

class MultipleObjectMixinBySponsor(MultipleObjectMixin):
    """
    This mixin filters the queryset in a list-view by request.user
    """
    # FIXME
    def get_queryset(self):
        queryset = super(MultipleObjectMixinBySponsor, self).get_queryset()
        queryset_by_user = queryset.filter(sponsor__single=self.request.user,sponsor__team_flag=False)
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

class UserTrends(MultipleObjectMixinByOwner,ListView):
    # FIXME
    model = Group
    template_name = 'ltuser/user_trends.tpl'
    context_object_name = 'groups'
    # def get_context_data(self, **kwargs):
    #     context = super(UserTrends, self).get_context_data(**kwargs)
    #     return context

class UserTeam(MultipleObjectMixinByMember,ListView):
    model = Team
    template_name = 'ltuser/user_team.tpl'
    context_object_name = 'teams'

class UserActivity(MultipleObjectMixinByParticipant,ListView):
    model = Activity
    template_name = 'ltuser/user_activity.tpl'
    context_object_name = 'activitys'
    paginate_by = 20

class UserParticipantActivity(MultipleObjectMixinByParticipant,ListView):
    model = Activity
    template_name = 'ltuser/user_participant_activity.tpl'
    context_object_name = 'activitys'
    paginate_by = 20

class UserOrganizerActivity(MultipleObjectMixinByOrganizer,ListView):
    model = Activity
    template_name = 'ltuser/user_organizer_activity.tpl'
    context_object_name = 'activitys'
    paginate_by = 20

class UserCreatorActivity(MultipleObjectMixinByCreator,ListView):
    model = Activity
    template_name = 'ltuser/user_creator_activity.tpl'
    context_object_name = 'activitys'
    paginate_by = 20

class UserMarkerActivity(MultipleObjectMixinByMarkActivity,ListView):
    model = Activity
    template_name = 'ltuser/user_marker_activity.tpl'
    context_object_name = 'activitys'
    paginate_by = 20

class UserSponsorActivity(MultipleObjectMixinBySponsor,ListView):
    model = Activity
    template_name = 'ltuser/user_sponsor_activity.tpl'
    context_object_name = 'activitys'
    paginate_by = 20

class UserMessageBoard(ListView):
    model = MessageBoard
    template_name = 'ltuser/user_messageboard'
    context_object_name = 'messageboard'
