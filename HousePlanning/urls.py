from django.urls import path
from HousePlanning import views
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    path('', views.IndexPage, name="index"),
    path('home', views.HomePage, name="home"),
    path('condo', views.CondoPage, name="condo"),
    path('logout', views.LogoutPage, name="logout"),
]
