from django.conf.urls import url, include, patterns

urlpatterns = patterns('characters.views',
    url(r'^$', 'characters_index', name='index'), # Main URL for list of all user's characters
    url(r'^create/$', 'characters_create', name='create'), # Create a character

    # Character profile URLs
    url(r'^(?P<pk>[\d]+)/', include(patterns('characters.views',
        url(r'^$', 'characters_show_index', name='index'),
        url(r'^items/$', 'characters_show_items', name='items'),
        url(r'^settings/$', 'characters_show_settings', name='settings'),
        url(r'^vehicles/$', 'characters_show_vehicles', name='vehicles'),
        url(r'^doors/$', 'characters_show_doors', name='doors'),
        url(r'^groups/$', 'characters_show_groups', name='groups'),
        url(r'^group-invitations/$', 'characters_show_group_invitations',
            name='group_invitations'),
        url(r'^group-invitations/(?P<invitation_id>[\d]+)/accept/$',
            'characters_show_group_invitations_accept',
            name='group_invitations_accept'),
        url(r'^group-invitations/(?P<invitation_id>[\d]+)/decline/$',
            'characters_show_group_invitations_decline',
            name='group_invitations_decline'),
    ), namespace='show'))
)
