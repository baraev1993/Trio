from rest_framework.serializers import ModelSerializer
from .models import Category, Film

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '_all_'

class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = '_all_'


