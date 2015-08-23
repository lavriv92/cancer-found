from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.PartnersListView.as_view(), name="list"),
]
