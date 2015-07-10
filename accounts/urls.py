from django.conf.urls import url, patterns, include

urlpatterns = patterns('accounts.views',
    url(r'^roleplay-test$', 'roleplay_test', name='roleplay-test')
)
