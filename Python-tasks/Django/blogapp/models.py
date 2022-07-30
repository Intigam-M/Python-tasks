from turtle import title, update
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)