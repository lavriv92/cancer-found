from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.ProjectsListView.as_view(), name="list"),
]
