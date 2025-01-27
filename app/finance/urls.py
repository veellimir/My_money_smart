from typing import List

from django.urls import path


from . import views
from settings.env_config import SUFFIX_API
from utils.suffix_router import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SUFFIX_API}{SuffixRouter.FINANCE}list-category', views.CategoryListView.as_view(), ),
    path(f'{SUFFIX_API}{SuffixRouter.FINANCE}create-category', views.CreateCategoryView.as_view(), )
]
