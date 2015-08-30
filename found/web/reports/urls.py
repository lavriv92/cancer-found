from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.ReportsListView.as_view(), name="list"),
]
