from typing import List
from django.urls import path

from . import views
from settings.settings import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SuffixRouter.FINANCE}operation-create', views.CreateOperationView.as_view(), ),
    path(f'{SuffixRouter.FINANCE}operation-list/<str:filter_params>', views.FinanceListView.as_view(), ),
]
