from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('about_us/<str:pk>/', views.about_us,name='about_us'),
]
