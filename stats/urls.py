from django.urls import path
from .views import RegisterView, StatsListCreateView, StatsUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('stats/', StatsListCreateView.as_view()),
    path('stats/<int:pk>/', StatsUpdateView.as_view()),
]