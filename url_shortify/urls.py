from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('url_shortify.views',
    url(r'^$', 'index'),
)
