from django.conf.urls import url, patterns, include

urlpatterns = patterns('accounts.views',
    url(r'^roleplay-test/$', 'roleplay_test', name='roleplay-test'),
    url(r'^login/$', 'accounts_login', name='login'),
    url(r'^logout/$', 'accounts_logout', name='logout'),
    url(r'^register/$', 'accounts_register', name='register'),
)
