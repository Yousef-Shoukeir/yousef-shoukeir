from django.contrib import admin
from django.urls import path
from .views import home, projects, contact, skills, about, wid

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='home'),
    path('contact/', contact, name='contact'),
    path('home/skills', skills, name='skills'),
    path('home/about', about, name='about'),
    path('home/what_i_do', wid, name='wid'),
]
