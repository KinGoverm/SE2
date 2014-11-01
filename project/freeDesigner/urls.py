from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


freeDesignerPatterns = patterns('freeDesigner.views',

	(r'^login/$', 'login'),
	('^$', 'main'),

)

urlpatterns =freeDesignerPatterns