from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    url('^', include('django.contrib.auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
