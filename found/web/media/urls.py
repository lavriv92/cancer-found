from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MediaView.as_view(), name='view'),
]
