from typing import List

from django.urls import path

from . import views
from settings.settings import SuffixRouter

urlpatterns: List[path] = [
    path(f'{SuffixRouter.USER}', views.CurrentUserView.as_view(), ),
    path(f'{SuffixRouter.USER}update', views.UpdateCurrentUserView.as_view(), ),
    path(f'{SuffixRouter.USER}set-image', views.SetImageUserView.as_view(), ),
    path(f'{SuffixRouter.USER}delete', views.DeleteCurrentUserView.as_view(), ),
    path(f'{SuffixRouter.USER}password-reset', views.PasswordResetRequestView.as_view(), name='password_reset_request'),
    path(f'{SuffixRouter.USER}password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path(f'{SuffixRouter.USER}final_password/', views.final_password, name='final_password'),

    path(f'{SuffixRouter.USER}politics/', views.politics_page, name='politics'),
]
