from django.urls import path, include
from main import views
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet

router = DefaultRouter()
router.register('film', FilmViewSet)

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='categories-list'),
    path('', include(router.urls))
    # path('film/', views.FilmView.as_view(), name='movies-list'),
    # path('film/<int:pk>/', views.FilmDetailView.as_view(), name='film-detail'),
    # path('film-update/<int:pk>/', views.FilmUpdateView.as_view(), name='film-update'),
    # path('film-delete/<int:pk>/', views.FilmDeleteView.as_view(), name='film-deletfilm')
]