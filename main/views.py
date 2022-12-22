from django.db.models import Q
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import generics

from .serializers import CategorySerializer, FilmSerializer
from .models import Category, Film




class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class FilmView(generics.ListCreateAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmDetailView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmUpdateView(generics.UpdateAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmDeleteView(generics.DestroyAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class= FilmSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()] # разрешаем только админам

    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        # /products/search/?q=hello
        # query_params = {'q':'hello'}
        q = request.query_params.get('q')
        queryset = self.get_queryset() # Product.objects.all()
        if q:
            # queryset = queryset.filter(title__icontains=q) # title ilike '%hello%'
            queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
            # title ilike '%hello%' or description ilike '%hello%'
        # get_serializer - ProductSerializer

        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)