from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^addressbook/', include('addressbook.urls', namespace="addressbook")),
    url(r'^admin/', include(admin.site.urls)),
)
