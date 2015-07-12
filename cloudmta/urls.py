from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^vehicles/', include('vehicles.urls', namespace='vehicles')),
]
