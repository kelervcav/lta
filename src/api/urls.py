from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^reviews/$', views.ReviewList.as_view()),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view()),

    url(r'^types/$', views.TypeList.as_view()),
    url(r'^types/(?P<pk>[0-9]+)/$', views.TypeDetail.as_view()),

    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),

    url(r'^devices/$', views.DeviceList.as_view()),
    url(r'^devices/(?P<pk>[0-9]+)/$', views.DeviceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
