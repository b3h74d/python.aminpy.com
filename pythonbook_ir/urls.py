from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin

import views


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^', include("contactus.urls")),
    (r'^pythonbook/$', views.toc),
    (r'^aboutpythonbook/$', views.about_book),
    (r'^admin/', include(admin.site.urls)),
    (r'^pythonbook(?P<number>\d\d)/$', views.controller),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
