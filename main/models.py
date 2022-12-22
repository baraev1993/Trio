from django.shortcuts import render
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=70)
    
    def __str__(self):
        return f'{self.title}'

class Film(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.PositiveIntegerField()
    poster = models.ImageField(upload_to='films', null=True)
    runtime = models.PositiveIntegerField()
    cast = models.TextField()
    category =models.ForeignKey(Category, related_name='film', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

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
    value = models.IntegerField()