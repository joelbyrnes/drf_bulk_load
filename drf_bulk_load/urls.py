from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from bulk_load import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'answers', views.AnswerList)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drf_bulk_load.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

	url(r'^', include(router.urls)),
	url(r'^answers/$', views.AnswerList.as_view()),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
