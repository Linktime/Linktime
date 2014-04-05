from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from api.urls import api

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','ltuser.views.index',name='index'),
    url(r'^register/$','ltuser.views.register',name='register'),
    url(r'^login/$',login,{'template_name':'ltuser/login.tpl'},name="login"),
    url(r'^logout/$','ltuser.views.ltlogout',name="logout"),
    url(r'^user/',include('ltuser.urls')),
    url(r'^activity/',include('activity.urls')),
    url(r'^friend/',include('friend.urls')),

    url(r'^api/',include(api.urls)),

    url(r'^mobile_register/$','ltuser.api.mobile_register',name='mobile_register'),
    url(r'^mobile_login/$','ltuser.api.mobile_login',name="mobile_login"),
    url(r'^test/','ltuser.views.test'),
    # Examples:
    # url(r'^$', 'Linktime.views.home', name='home'),
    # url(r'^Linktime/', include('Linktime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
