__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from rest_framework import routers

from etag.views import ReadersViewSet


router = routers.SimpleRouter()
router.register('readers', ReadersViewSet)
#router.register('lusource', LuSourceViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
