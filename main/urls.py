# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('auth/', views.auth, name='auth'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register')
]

