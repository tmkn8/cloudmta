from django.conf.urls import url, patterns
urlpatterns = patterns('wiki.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<cat>[\w]+)/$', 'category', name='category'),
    url(r'^(?P<cat>[\w]+)/(?P<article>[\w]+)/$', 'article', name='article'),
)
