from typing import List

from django.urls import path

from . import views
from settings.settings import SuffixRouter


urlpatterns: List[path] = [
    path(f'{SuffixRouter.STATISTIC}list/<str:date>', views.StatisticView.as_view(), )
]
