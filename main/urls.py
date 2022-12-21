from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, FilmViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('film', FilmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]