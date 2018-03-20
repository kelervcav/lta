from django.conf.urls import url
from .views import (
    TypeGroupListView, TypeListView, DeviceListView,
    LocationListView
)
from . import views


urlpatterns = [
    # Type Group
    url(r'^type-group/$', TypeGroupListView.as_view(), name='typegroup_list'),
    url(r'^type-group/create/$',
        views.typegroup_create, name='typegroup_create'),
    url(r'^type-group/(?P<pk>\d+)/edit/$',
        views.typegroup_edit, name='typegroup_update'),

    # Type
    url(r'^type/$', TypeListView.as_view(), name='type_list'),
    url(r'^type/create/$',
        views.type_create, name='type_create'),
    url(r'^type/(?P<pk>\d+)/edit/$',
        views.type_edit, name='type_update'),

    # Type
    url(r'^device/$', DeviceListView.as_view(), name='device_list'),
    url(r'^device/create/$',
        views.device_create, name='device_create'),
    url(r'^device/(?P<pk>\d+)/edit/$',
        views.device_edit, name='device_update'),

    # Location
    url(r'^location/$', LocationListView.as_view(), name='location_list'),
    url(r'^location/create/$',
        views.location_create, name='location_create'),
    url(r'^location/(?P<pk>\d+)/edit/$',
        views.location_edit, name='location_update'),
]
