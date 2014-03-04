from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'nannies_ca.views.home', name='home'),
    url(r'^about/', 'nannies_ca.views.about', name='about'),
    url(r'^faq/', 'nannies_ca.views.faq', name='faq'),
    url(r'^contact/', 'nannies_ca.views.contact', name='contact'),
    url(r'^news/', 'nannies_ca.views.news', name='news'),

    # user auth urls
    url(r'^login/', 'nannies_ca.views.login', name='login'),
    url(r'^auth/', 'nannies_ca.views.auth_view', name='auth_view'),
    url(r'^invalid/', 'nannies_ca.views.invalid', name='invalid'),
    url(r'^family/', 'nannies_ca.views.family', name='family'),

    url(r'^admin/', include(admin.site.urls)),
)
