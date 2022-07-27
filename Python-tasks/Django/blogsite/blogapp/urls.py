from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post', views.post,  name="post"),
    path('post-detal', views.postDetal,  name="post-detal"),
]
