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
    video = models.FileField(upload_to='video',null=True)

    def __str__(self):
        return f'{self.name}'
    