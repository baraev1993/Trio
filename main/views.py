from django.shortcuts import render

# Create your views here.

class Rating(models.Model):
    user = models.IntegerField()
    film = models.IntegerField()
    value = models.enums()