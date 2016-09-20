from django.conf.urls import url

from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home),
    url(r'^show$', views.show),
    url(r'^store$', views.store),
    url(r'^delete$', views.delete),
]
