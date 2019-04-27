from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello_world', views.HelloWorld.as_view())
]