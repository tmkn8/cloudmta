from django.conf.urls import url, patterns

urlpatterns = patterns('doors.views',
    url(r'^(?P<pk>[\d]+)/$', 'doors_show', name='show')
)
