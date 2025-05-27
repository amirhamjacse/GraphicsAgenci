from django.conf.urls.static import static
from django.urls import path, include
from urlshortner import views

urlpatterns = [
    path('', views.home, name='home'),
]
  
