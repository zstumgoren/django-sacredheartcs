from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from sacredheartcs.config.base.urls import urlpatterns

admin.autodiscover()

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
