from typing import List

from django.urls import path


from . import views
from settings.env_config import SUFFIX_API

urlpatterns: List[path] = [
    path(f'{SUFFIX_API}user/', views.CurrentUserView.as_view(), ),
    path(f'{SUFFIX_API}user/update', views.UpdateCurrentUserView.as_view(), ),
    path(f'{SUFFIX_API}user/set-image', views.SetImageUserView.as_view(), )
]
