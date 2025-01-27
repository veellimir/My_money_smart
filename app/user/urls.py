from typing import List

from django.urls import path

from . import views
from settings.settings import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SuffixRouter.USER}', views.CurrentUserView.as_view(), ),
    path(f'{SuffixRouter.USER}update', views.UpdateCurrentUserView.as_view(), ),
    path(f'{SuffixRouter.USER}set-image', views.SetImageUserView.as_view(), )
]
