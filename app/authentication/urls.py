from typing import List

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from settings.env_config import SUFFIX_API
from utils.suffix_router import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SUFFIX_API}{SuffixRouter.AUTH}', views.RegisterUserView.as_view(), ),
    path(f'{SUFFIX_API}{SuffixRouter.AUTH}login', TokenObtainPairView.as_view(), ),
    path(f'{SUFFIX_API}{SuffixRouter.AUTH}refresh', TokenRefreshView.as_view(), ),
    path(f'{SUFFIX_API}{SuffixRouter.AUTH}change-password', views.NewUserPasswordView.as_view(), ),
]
