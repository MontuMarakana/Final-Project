from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.index),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact,name='contact'),
    path('userlogout/',views.userlogout),
   
]
