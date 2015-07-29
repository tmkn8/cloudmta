from django.conf.urls import url, patterns

urlpatterns = patterns('pages.views',
    url(r'^gui/$', 'gui', name='gui'),
)
