from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^(?:page-(?P<page>[\d]+)/)?$', 'index', name='index'),
    url(r'^(?P<slug>[\w]+)/$', 'post', name='post'),
)
