from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path("", views.index, name='index'),
    path("bengali", views.bengali, name='bengali'),
    path("hindi", views.hindi, name='hindi'),
    path("english", views.english, name='english'),
]
