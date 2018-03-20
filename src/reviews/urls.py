from django.conf.urls import url
from .views import ReviewListView


urlpatterns = [
    # Reviews
    url(r'^$', ReviewListView.as_view(), name='list'),
]
