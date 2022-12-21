from django.shortcuts import render
from .models import models

class Comment(models.Model):
    user = models.IntegerField()
    body = models.TextField()
    craeted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)        

class Rating(models.Model):
    user = models.IntegerField()
    film = models.IntegerField()
    value = models.enums()