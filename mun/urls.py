from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mun_form, name='mun_form'),
]