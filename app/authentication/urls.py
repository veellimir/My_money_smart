from typing import List

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from settings.settings import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SuffixRouter.AUTH}', views.RegisterUserView.as_view(), ),
    path(f'{SuffixRouter.AUTH}login', TokenObtainPairView.as_view(), ),
    path(f'{SuffixRouter.AUTH}refresh', TokenRefreshView.as_view(), ),
    path(f'{SuffixRouter.AUTH}change-password', views.NewUserPasswordView.as_view(), ),
]
