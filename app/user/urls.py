from typing import List

from django.urls import path


from . import views
from settings.env_config import SUFFIX_API
from utils.suffix_router import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SUFFIX_API}{SuffixRouter.USER}', views.CurrentUserView.as_view(), ),
    path(f'{SUFFIX_API}{SuffixRouter.USER}update', views.UpdateCurrentUserView.as_view(), ),
    path(f'{SUFFIX_API}{SuffixRouter.USER}set-image', views.SetImageUserView.as_view(), )
]
