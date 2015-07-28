from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'characters.views.characters_index', name='homepage'),
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^vehicles/', include('vehicles.urls', namespace='vehicles')),
    url(r'^groups/', include('groups.urls', namespace='groups')),
    url(r'^doors/', include('doors.urls', namespace='doors')),
]
