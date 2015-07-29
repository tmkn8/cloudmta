from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Django
    url(r'^admin/', include(admin.site.urls)),

    # Mine
    url(r'^$', 'pages.views.homepage', name='homepage'),
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^vehicles/', include('vehicles.urls', namespace='vehicles')),
    url(r'^groups/', include('groups.urls', namespace='groups')),
    url(r'^doors/', include('doors.urls', namespace='doors')),
    url(r'^page/', include('pages.urls', namespace='pages')),
    url(r'^wiki/', include('wiki.urls', namespace='wiki')),

    # Third-party
]
