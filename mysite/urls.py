from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'mysite.mainapp.views.index'),
    (r'^about$', 'mysite.mainapp.views.about'),
    (r'^everything$', 'mysite.mainapp.views.everything'),
    (r'^view/(?P<thing__pk>\d+)$', 'mysite.mainapp.views.view_thing'),
    (r'^tag/(?P<tag__pk>\d+)$', 'mysite.mainapp.views.view_tag'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
)
