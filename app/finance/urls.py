from typing import List

from django.urls import path

from . import views
from settings.settings import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SuffixRouter.FINANCE}create-category', views.CreateCategoryView.as_view(), ),
    path(f'{SuffixRouter.FINANCE}delete-category/<int:pk>', views.DeleteCategoryView.as_view(), ),
    path(f'{SuffixRouter.FINANCE}list-category', views.CategoryListView.as_view(), ),
]
