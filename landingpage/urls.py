from django.contrib import admin
from django.urls import path
from landingpage import views
from landingpage.views import ProjectDetailView

urlpatterns = [
    path('', views.LandPageView.as_view(), name='index'),
    path('contact/', views.contact_us_view, name='contact_us'),
    path('case-study/<int:pk>/', views.BrandingCaseStudyDetailView.as_view(), name='branding_case_study_detail'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    # path('land/', views.IndexView.as_view(), name='land'),
]