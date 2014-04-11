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
from django.db.models import Q

import json
import datetime

from activity.models import Activity, ActivityTicketType,ActivityTicket, ActivityTeamTicket, ActivityOrganizerList, ActivityTask, ActivitySingleOrganizer
from activity.forms import ActivityCreateForm
from activity.util import get_qrcode

from place.models import Lbs

from tastypie.models import ApiKey

class SingleObjectMixinByOrganizer(SingleObjectMixin):
    """
    This mixin checks object ownership in detail-view or delete-view
    """
    def get_object(self):
        object = super(SingleObjectMixinByOrganizer, self).get_object()
        user = auth.get_user(self.request)
        organizer_list = object.organizer_list_activity.filter(Q(single=user)|Q(team__member=user))
        if organizer_list:
            return object
        else:
            raise Http404

class SingleObjectMixinByOrganizerAndPreparing(SingleObjectMixin):
    """
    This mixin checks object ownership in detail-view or delete-view
    """
    def get_object(self):

        object = super(SingleObjectMixinByOrganizerAndPreparing, self).get_object()
        user = auth.get_user(self.request)
        if object.preparing:
            if not user.is_anonymous():
                organizer_list = object.organizer_list_activity.filter(Q(single=user)|Q(team__member=user))
                if organizer_list:
                    return object
            raise Http404
        else :
            return object

class ActivityListView(ListView):
    model = Activity
    template_name = 'activity/activity_listview.tpl'
    context_object_name = 'activitys'
    paginate_by = 15

class ActivitySearchListView(ListView):
    model = Activity
    template_name = 'activity/activity_search_listview.tpl'
    context_object_name = 'activitys'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ActivitySearchListView,self).get_context_data(**kwargs)
        activity_name = self.request.GET.get("activity_name")
        activity = self.get_queryset()
        if activity_name:
            context['activitys'] = activity.filter(name__contains=activity_name)
        return context

class ActivitySearchMapListView(ListView):
    model = Activity
    template_name = 'activity/activity_search_map_listview.tpl'
    context_object_name = 'activitys'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ActivitySearchMapListView,self).get_context_data(**kwargs)
        lat = self.request.GET.get("lat")
        lng = self.request.GET.get("lng")
        activity = self.get_queryset()
        if lat and lng:
            lat = float(lat)
            lng = float(lng)
            # context['activitys'] = activity.filter(Q(lbs__lat__le=lat))
            points = [{'lat':lat-0.002,'lng':lng-0.002},
                     {'lat':lat+0.002,'lng':lng-0.002},
                     {'lat':lat-0.002,'lng':lng+0.002}]
            pass
            context['points'] = points
            context['search_point'] = {'lat':lat,'lng':lng}
        else:
            del context["activitys"]
        return context


class ActivityDetailView(SingleObjectMixinByOrganizerAndPreparing,DetailView):
    model = Activity
    template_name = 'activity/activity_detailview.tpl'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super(ActivityDetailView,self).get_context_data(**kwargs)
        user = auth.get_user(self.request)
        if not user.is_anonymous():
            organizer = context['activity'].organizer_list_activity.filter(Q(single=self.request.user)|Q(team__member=self.request.user))
            if organizer:
                context['organizer'] = True

        ticket_types = context['activity'].tickettype_activity.filter()
        context['ticket_types'] = ticket_types
        return context

class ActivityManageDetailView(DetailView,SingleObjectMixinByOrganizer):
    model = Activity
    template_name = 'activity/activity_manage_detailview.tpl'
    context_object_name = 'activity'

class ActivityParticipantDetailView(DetailView,SingleObjectMixinByOrganizer):
    model = Activity
    template_name = 'activity/activity_manage_participant.tpl'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super(ActivityParticipantDetailView,self).get_context_data(**kwargs)
        activity = context['activity']
        context['activity_tickettype'] = ActivityTicketType.objects.filter(activity=activity)
        return context

class ActivityStatisticsDetailView(DetailView,SingleObjectMixinByOrganizer):
    model = Activity
    template_name = 'activity/activity_manage_statistics.tpl'
    context_object_name = 'activity'

class ActivityTaskDetailView(DetailView,SingleObjectMixinByOrganizer):
    model = Activity
    template_name = 'activity/activity_manage_task.tpl'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super(ActivityTaskDetailView,self).get_context_data(**kwargs)
        activity = context['activity']
        context['tasks'] = activity.activitytask_activity.filter()
        return context

class ActivityOptionsDetailView(DetailView,SingleObjectMixinByOrganizer):
    model = Activity
    template_name = 'activity/activity_manage_options.tpl'
    context_object_name = 'activity'

class ActivityMapView(DetailView):
    model = Activity
    template_name = 'activity/activity_map.tpl'
    context_object_name = 'activity'

class ActivityQrCodeView(DetailView):
    model = Activity
    template_name = 'activity/activity_qrcode.tpl'
    context_object_name = 'activity'

@login_required
def activity_qrcode(request,pk):
    at = ActivityTicket.objects.all()[0]
    qr = get_qrcode(at)
    return HttpResponse(qr,mimetype='image/png')

# DIY
def mobile_get_qrcode(request,pk,tid):
    username = request.GET.get("username")
    api_key = request.GET.get("api_key")
    try:
        user = User.objects.get(username=username)
        apikey = ApiKey.objects.get(user=user,key=api_key)
        activity = Activity.objects.get(id=pk)
        activity_ticket_type = ActivityTicketType.objects.filter(activity=activity)
        ticket = ActivityTicket.objects.get(owner=user,type=activity_ticket_type[0])
        # FIXME
        return HttpResponse(get_qrcode(ticket),mimetype='image/png')
    except:
        return HttpResponseForbidden()

def mobile_activity_nearby(request):
    return render_to_response('activity/mobile_activity_nearby.tpl')

@login_required()
def activity_create(request):
    if request.method == 'GET':
        form = ActivityCreateForm()
    else:
        form = ActivityCreateForm(request.POST)
        # FIXME
        lat = request.POST.get("lat")
        lng = request.POST.get("lng")
        if form.is_valid():
            activity = form.save(commit=False)
            activity.creator = request.user
            activity.lbs = Lbs.objects.create(lat=float(lat),lng=float(lng))
            activity.save()
            organizer_list = ActivityOrganizerList.objects.create(activity=activity)
            organizer_single = ActivitySingleOrganizer.objects.create(organizer_list=organizer_list,user=request.user)
            messages.success(request, u'活动已创建成功！')
            return HttpResponseRedirect(reverse('activity_manage', kwargs={'pk': activity.id}))
        else:
            messages.warning(request, u'请重新确认您输入的信息是否有误！%s'%form.errors)
    return render_to_response('activity/activity_create.tpl', {'form': form}, context_instance=RequestContext(request))

@login_required
def activity_release(request,pk):
    activity = Activity.objects.get(id=pk)
    user = request.user
    try :
        organizer = activity.organizer_list_activity.filter(Q(single=user)|Q(team__member=user))
        if organizer:
            activity.preparing = False
            activity.save()
            return HttpResponseRedirect(reverse('activity_detail',kwargs={'pk':pk}))
    except :
        pass
    return HttpResponseRedirect(reverse('activity_manage',kwargs={'pk':pk}))

@login_required
@csrf_exempt
def activity_single_join(request,pk):
    activity = activity = Activity.objects.get(id=pk)
    type = request.POST.get('type')
    type = activity.tickettype_activity.get(type=type)
    try:
        activity_ticket = ActivityTicket.objects.get(owner=request.user,type=type)
    except :
        activity_ticket = ActivityTicket.objects.create(owner=request.user,type=type)
    messages.success(request, u'你已报名成功！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))


@login_required()
def activity_single_join_cancel(request, pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        type = request.POST.get('type')
        type = activity.tickettype_activity.get(type=type)
        try :
            activity_ticket = ActivityTicket.objects.get(owner=request.user,type=type)
            activity_ticket.delete()
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
        user.ltuser.mark_activity.add(activity)
        messages.info(request, u'你已成功收藏！')
    except Activity.DoesNotExist:
        messages.success(request, u'您要收藏的活动不存在，请重新确认！')
    return HttpResponseRedirect(reverse('activity_detail', kwargs={'pk': pk}))

@login_required()
def activity_mark_cancel(request,pk):
    try:
        user = request.user
        activity = Activity.objects.get(id=pk)
        user.ltuser.mark_activity.remove(activity)
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