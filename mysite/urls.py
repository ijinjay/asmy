from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings
from django.conf.urls.static import static
# Include these import statements...
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$',hello),
	('^query/$','views.query'),
	('^index/$','views.index'),
	('^vip_consume/$','views.vip_consume'),
	('^non_vip/$','views.non_vip'),
	('^add_money/$','views.add_money'),
	('^my_view/$','views.my_view'),
	('^logout_view/$','views.logout_view'),
	('^regist_user_page/$','views.regist_user_page'),
	('^regist_designer_page/$','views.regist_designer_page'),
	('^designer_log/$','views.designer_log'),
	('^regist_user/$','views.regist_user'),
	('^regist_designer/$','views.regist_designer'),
	('^error/$','views.error'),
    ('^admin/', include(admin.site.urls)),
    ('^accounts/login/$', 'django.contrib.auth.views.login',{'templates': 'login.html'}),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# static is used for the location of static files--
