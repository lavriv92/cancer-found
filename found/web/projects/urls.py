from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProjectsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='detail')
]
