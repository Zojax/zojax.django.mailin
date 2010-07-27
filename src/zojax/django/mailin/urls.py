from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('zojax.django.mailin',
    url(r'^mailinTransport$', 'transport.transport', name='mailin-transport'),
    url(r'^mailloader$', 'mailloader_views.loader', name='mailin-loader'),
    url(r'^mailloader.py$', 'mailloader_views.loader_py', name='mailin-loader-script'),
)
