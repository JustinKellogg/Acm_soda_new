from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ('^$', 'acm_soda.web.views.external'),
    ('profile/$', 'acm_soda.web.views.profile'),
    ('profile/(?P<username>(\d|\w)+)', 'acm_soda.web.views.profile'),
    ('purchase/$', 'acm_soda.web.views.purchase'),
    ('logout/', 'acm_soda.web.views.profile_logout'),
    ('login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
