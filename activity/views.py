# -*- coding:utf-8 -*-
# Create your views here.
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, Http404
from django.contrib.admin.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

import json
import datetime

from activity.models import Activity, GenericMember, GenericOrganizer
from activity.forms import ActivityCreateForm

class SingleObjectMixinByOrganizer(SingleObjectMixin):
    """
    This mixin checks object ownership in detail-view or delete-view
    """
    def get_object(self):
        object = super(SingleObjectMixinByOrganizer, self).get_object()
        organizer = object.organizer.filter(single=self.request.user,team_flag=False)
        if organizer:
            return object
        else:
            raise Http404

class MultipleObjectMixinByParticipant(MultipleObjectMixin):
    """
    This mixin filters the queryset in a list-view by request.user
    """
    def get_queryset(self):
        queryset = super(MultipleObjectMixinByParticipant, self).get_queryset()
        queryset_by_user = queryset.filter(participant__single=self.request.user,team_flag=False)
        return queryset_by_user

class ActivityListView(ListView):
    model = Activity
    template_name = 'activity/activity_listview.tpl'
    context_object_name = 'activitys'
    paginate_by = 20


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity/activity_detailview.tpl'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super(ActivityDetailView,self).get_context_data(**kwargs)
        user = auth.get_user(self.request)
        if not user.is_anonymous():
            organizer = context['activity'].organizer.filter(single=self.request.user,team_flag=False)
            if organizer:
                context['organizer'] = True
        return context

class ActivityManageDetailView(DetailView,SingleObjectMixinByOrganizer):
    model = Activity
    template_name = 'activity/activity_manage_detailview.tpl'
    context_object_name = 'activity'

class ActivityParticipantDetailView(DetailView,SingleObjectMixinByOrganizer):
    model = Activity
    template_name = 'activity/activity_participant.tpl'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super(ActivityParticipantDetailView,self).get_context_data(**kwargs)
        context['participants'] = context['activity'].participant.filter()
        return context

class ActivityMapView(DetailView):
    model = Activity
    template_name = 'activity/activity_map.tpl'
    context_object_name = 'activity'

class ActivityQrCodeView(DetailView):
    model = Activity
    template_name = 'activity/activity_qrcode.tpl'
    context_object_name = 'activity'


@login_required()
def activity_create(request):
    if request.method == 'GET':
        form = ActivityCreateForm()
    else:
        form = ActivityCreateForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.creator = request.user
            activity.save()
            generic_object = GenericOrganizer.objects.create(single=request.user)
            activity.organizer.add(generic_object)
            messages.success(request, u'活动已创建成功！')
            return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': activity.id}))
        else:
            messages.warning(request, u'请重新确认您输入的信息是否有误！%s'%form.errors)
    return render_to_response('activity/activity_create.tpl', {'form': form}, context_instance=RequestContext(request))


@login_required()
def activity_join(request, pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        user_object = activity.participant.filter(single=request.user,team_flag=False)
        if user_object:
            messages.info(request, u'你已报名成功，无须重复报名')
        else:
            user_object = GenericOrganizer.objects.create(single=request.user)
            activity.participant.add(user_object)
            messages.success(request, u'你已报名成功！')
    except Activity.DoesNotExist:
        messages.error(request, u'您要参加的活动不存在，请重新确认！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))


@login_required()
def activity_join_cancel(request, pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        try :
            user_object = activity.participant.get(single=request.user.id,team_flag=False)
            activity.participant.remove(user_object)
            messages.info(request, u'你已取消报名！')
        except:
            messages.warning(request, u'你未报名该活动！')

    except Activity.DoesNotExist:
        messages.error(request, u'您要取消参加的活动不存在，请重新确认！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))

@login_required()
def activity_mark(request,pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        activity.marker.add(user)
        messages.info(request, u'你已成功收藏！')
    except Activity.DoesNotExist:
        messages.success(request, u'您要收藏的活动不存在，请重新确认！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))

@login_required()
def activity_mark_cancel(request,pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        activity.marker.remove(user)
        messages.info(request, u'你已取消收藏！')
    except Activity.DoesNotExist:
        messages.error(request, u'您要取消收藏的活动不存在，请重新确认！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))


# FIXME
# ------------------------------------------
@login_required()
def activity_support(request, pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        if user in activity.sponsor.all():
            messages.info(request, u'你已为％s提供赞助，请勿重复提交！' % activity.name)
        else:
            activity.sponsor.add(user)
            messages.success(request, u'你已为％s提供赞助！' % activity.name)
    except Activity.DoesNotExist:
        messages.error(request, u'您要赞助的活动不存在，请重新确认！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))


@login_required()
def activity_support_cancel(request, pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        activity.sponsor.remove(user)
        messages.info(request, u'你已取消为％s提供赞助！' % activity.name)
    except Activity.DoesNotExist:
        messages.error(request, u'您要取消赞助的活动不存在，请重新确认！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))
# -------------------------------------------------------------

# FIXME
# This function should server for ajax
# -------------------------------------------------------------------------------------
@login_required()
def activity_organizer_add(request, pk):
    if request.method == 'POST':
        activity = Activity.objects.get(id=pk)
        data = json.loads(request.POST) # TO CHECK
        for organizer_id in data['organizers_id']:
            try:
                organizer = User.objects.get(id=organizer_id)
                activity.organizer.add(organizer)
            except User.DoseNotExist:
                pass
                # FIXME Should return a html page
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))


@login_required()
def activity_organizer_cancel(request, pk):
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))

# -------------------------------------------------------------------------------------

@csrf_exempt
def ajax_activity_update(request,pk):
    # import code;code.interact(local=locals())
    try:
        activity = Activity.objects.get(id=pk)
        if request.POST['name'] == u'date':
            activity.__dict__[request.POST['name']] = datetime.datetime.strptime(request.POST['value'],"%Y-%m-%d").date()
            activity.save()
        else :
            activity.__dict__[request.POST['name']] = request.POST['value']
            activity.save()
        return HttpResponse()
    except :
        messages.error(request,u"更新失败，如多次出现该提示，请联系管理员")
        return HttpResponseRedirect(reverse('activity_detail',kwargs={'pk':pk}))