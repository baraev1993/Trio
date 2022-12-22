from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterUserView,activate_view



urlpatterns = [
    # path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('activate/<str:activation_code>/', activate_view),
]