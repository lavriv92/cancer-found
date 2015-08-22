from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^contacts/$', views.ContactsView.as_view(), name='contacts'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]
