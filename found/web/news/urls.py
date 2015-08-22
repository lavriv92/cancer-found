from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.NewsListView.as_view(), name="list"),
]
