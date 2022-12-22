from django.shortcuts import render
from rest_framework.viewsets import generics

from .models import Category, Film

from .serializers import CategorySerializer, FilmSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FilmView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetailView(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmUpdateView(generics.UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDeleteView(generics.DestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer