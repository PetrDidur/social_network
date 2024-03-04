from django.urls import path

from .apps import UsersConfig
from .views import UserDetailAPI, RegisterUserAPIView, UserListAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserRetrieveAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name


urlpatterns = [
  path("get-details/", UserDetailAPI.as_view(), name="user-detail"),
  path('register/', RegisterUserAPIView.as_view(), name='register'),
  path('user/', UserListAPIView.as_view(), name='user-list'),
  path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
  path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
]