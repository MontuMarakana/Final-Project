from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.index),
    path('home/',views.home,name='home'),
    path('userlogout/',views.userlogout),
   
]
