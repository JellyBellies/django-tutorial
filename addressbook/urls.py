from django.conf.urls import patterns, url

from addressbook import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<record_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^addrecord/$', views.addrecord, name="addrecord"),
    url(r'^submitrecord/$', views.submitrecord, name="submitrecord"),
)
