from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Category, Film
from .serializers import CategorySerializer, FilmSerializer

class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class= FilmSerializer

class CategoryViewSet(ModelViewSet):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer

