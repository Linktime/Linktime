# -*- coding:utf-8 -*-

from tastypie.resources import ModelResource, ALL
from tastypie.models import ApiKey
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.authentication import Authentication, ApiKeyAuthentication
from tastypie.authorization import Authorization

from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import login, authenticate

class UserObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.user == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        #return bundle.obj.user == bundle.request.user
        return True

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        #raise Unauthorized("Sorry, no deletes.")
        return object_list.filter(user=bundle.request.user)

    def delete_detail(self, object_list, bundle):
        #raise Unauthorized("Sorry, no deletes.")
        return bundle.obj.user == bundle.request.user

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.select_related().filter()
        resource_name = "ltuser/user"
        allowed_method = ['get',]
        serializer = Serializer(formats=['json',])
        excludes = ['password','is_active','is_staff','is_superuser','first_name','last_name']
        authentication = ApiKeyAuthentication()
        filtering = {
            'username':ALL,
        }

@csrf_exempt
def mobile_register(request):
    register_success = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        response = HttpResponse()
        try :
            user = User.objects.get(username=username)
            if user:
                response['register_status'] = 1
                return response
        except :
            pass
        response['register_status'] = 0
        user = User.objects.create_user(username=username,password=password)
        api_key = ApiKey.objects.get(user=user)
        response['API_Key'] = api_key.key
        return response
    else :
        return HttpResponseForbidden()

@csrf_exempt
def mobile_login(request):
    login_success = False
    username = request.POST['username']
    password = request.POST['password']
    response = HttpResponse()
    response['Auth_Response'] = 0
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        response['Auth_Response'] = 1
    try :
        user = authenticate(username=username,password=password)
        if not user is None:
            login(request,user)
            login_success = True
    except BaseException,e:
        print e
        response['Auth_Response'] = 2
    try:
        api_key = ApiKey.objects.get(user=user)
        response['API_Key'] = api_key.key
    except :
        pass
    return response