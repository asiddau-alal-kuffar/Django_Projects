from django.contrib import admin
from django.urls import path
from .views import *

admin.site.site_header = 'Student_Records_Management_System(SRMS)'
admin.site.index_title = 'WELCOME To Student Records Management System !'
admin.site.site_title = 'Student Records Management System'

urlpatterns = [
    path('', home),
    path('index/',index),
    path('Education/',Education),
    path('Register/',Register),
    path('Login/',Login),
    path('StudentIdCards',StudentIdCards)
]