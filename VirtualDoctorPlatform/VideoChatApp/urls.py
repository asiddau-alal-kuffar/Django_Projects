from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('Login/',Login),
    path('Logout/',LogOut),
    
]
