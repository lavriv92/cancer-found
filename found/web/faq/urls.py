from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.FaqView.as_view(), name='view')
]
