from django.urls import path, include
from main import views
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet

router = DefaultRouter()
router.register('film', FilmViewSet)

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='categories-list'),
    path('', include(router.urls))
   
]