from django.contrib import admin
from django.urls import path
from landingpage import views

urlpatterns = [
    path('', views.LandPageView.as_view(), name='index'),
    path('land/', views.IndexView.as_view(), name='land'),
    path('contact/', views.contact_us_view, name='contact_us'),
]


