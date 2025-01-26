from typing import List

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from settings.env_config import SUFFIX_API

urlpatterns: List[path] = [
    path(f'{SUFFIX_API}authentication/', views.RegisterUserView.as_view(), ),
    path(f'{SUFFIX_API}authentication/login', TokenObtainPairView.as_view(), ),
    path(f'{SUFFIX_API}authentication/refresh', TokenRefreshView.as_view(), ),
]
