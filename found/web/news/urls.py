from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.NewsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.NewsDetailView.as_view(), name='detail')
]
