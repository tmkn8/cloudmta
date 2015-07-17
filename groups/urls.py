from django.conf.urls import url, include, patterns

urlpatterns = patterns('groups.views',
    url(r'^(?P<pk>[\d]+)/', include(patterns('groups.views',
        url(r'^$', 'groups_show_index', name='index'),
        url(r'^members$', 'groups_show_members', name='members'),
        url(r'^ranks$', 'groups_show_ranks', name='ranks'),
    ), namespace='show')),
)