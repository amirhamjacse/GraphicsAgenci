from django.contrib import admin
from django.urls import path
from landingpage import views

urlpatterns = [
    path('', views.LandPageView.as_view(), name='index'),
    path('contact/', views.contact_us_view, name='contact_us'),
    # path('land/', views.IndexView.as_view(), name='land'),
]