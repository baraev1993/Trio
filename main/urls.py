from django.urls import path
from main import views



urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='categories-list'),
    path('film/', views.FilmView.as_view(), name='movies-list'),
    path('film/<int:pk>/', views.FilmDetailView.as_view(), name='film-detail'),
    path('film-update/<int:pk>/', views.FilmUpdateView.as_view(), name='film-update'),
    path('film-delete/<int:pk>/', views.FilmDeleteView.as_view(), name='film-deletfilm')]