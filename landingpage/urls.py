from django.contrib import admin
from django.urls import path
from landingpage import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('land/', views.LandPageView.as_view(), name='index'),
]


