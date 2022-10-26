from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from demoapp.views import *
urlpatterns = [
    
    path('photo', views.photo_view, name='photo'),
    
]
