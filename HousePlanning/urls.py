from django.urls import path
from HousePlanning import views
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    path('', views.IndexPage, name="index"),
    path('', views.HomePage, name="home"),
]

