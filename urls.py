from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('acm_soda.web.urls')),
    (r'^web/', include('acm_soda.web.urls')), #remaining portion of URL sent to web/api
    (r'^api/', include('acm_soda.api.urls')),
    
    #Admin page
    (r'^admin/(.*)', admin.site.root),
    
    #dev server media
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': '/Users/josheads/code/acm_soda/media/'}),
)
