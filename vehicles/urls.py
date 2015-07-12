from django.conf.urls import url, patterns

urlpatterns = patterns('vehicles.views',
    url(r'^(?P<pk>[\d]+)$', 'vehicles_show', name='show'),
)
