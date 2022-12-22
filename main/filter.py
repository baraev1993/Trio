from django_filters.rest_framework import FilterSet
import django_filters

from .models import Film


class FilmFilter(FilterSet):
    category_title = django_filters.CharFilter(field_name='category__title')
    category_id = django_filters.NumberFilter(field_name='category')

    class Meta:
        model = Film
        fields = ['category_title', 'category_id']
    