from django.conf.urls import patterns, include, url
from django.contrib import admin
import dnaedit

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangopython.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dnaedit/',include('dnaedit.urls', namespace='dnaedit')),
    url(r'^media/images/(?P<imageName>[^/]+)/$', dnaedit.views.imageShow, )
)
