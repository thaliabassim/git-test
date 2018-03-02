from django.urls import path 
from . import views

urlpatterns = [
path('', views.homepageview.as_view(), name = 'home'),
path('about/', views.aboutview.as_view(), name = 'about'),

]