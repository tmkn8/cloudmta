from django.conf.urls import url, include, patterns

urlpatterns = patterns('groups.views',
    url(r'^(?P<pk>[\d]+)/', include(patterns('groups.views',
        url(r'^$', 'groups_show_index', name='index'),

        url(r'^members/$', 'groups_show_members', name='members'),
        url(r'^members/(?P<member_id>[\d]+)$', 'groups_show_members_edit',
            name='members_edit'),
        url(r'^members/(?P<member_id>[\d]+)/delete/$',
            'groups_show_members_delete', name='members_delete'),

        url(r'^ranks/$', 'groups_show_ranks', name='ranks'),
        url(r'^ranks/(?P<rank_id>[\d]+)$', 'groups_show_ranks_edit',
            name='ranks_edit'),
        url(r'^ranks/(?P<rank_id>[\d]+)/delete/$', 'groups_show_ranks_delete',
            name='ranks_delete'),

        url(r'^ranks/default-rank/$', 'groups_show_ranks_default_rank',
            name='ranks_default_rank'),

        url(r'^invitations/$', 'groups_show_invitations', name='invitations'),
        url(r'^invitations/create/$', 'groups_show_invitations_create',
            name='invitations_create'),
        url(r'^invitations/(?P<invitation_id>[\d]+)/delete/$',
            'groups_show_invitations_delete', name='invitations_delete'),
    ), namespace='show')),
)
