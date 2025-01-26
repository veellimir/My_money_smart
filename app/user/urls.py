from typing import List

from django.urls import path


from . import views
from settings.env_config import SUFFIX_API

urlpatterns: List[path] = [
    path(f'{SUFFIX_API}user/', views.CurrentUserView.as_view(), )
]
