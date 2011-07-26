from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('url_shortify.views',
    url(r'^$', 'index'),
    url(r'^(?P<short>[0-9a-zA-Z]+)/$', 'unshortify'),
)
