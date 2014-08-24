from django.conf.urls import patterns, include, url



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'log.html'}, name='login'),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page': '/accounts/login/'},name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
