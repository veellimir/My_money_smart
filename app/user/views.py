from rest_framework import generics

from repository.base_queryset import BaseCurrentUser
from .serializers import (
    CurrentUserSerializer,
    UpdateCurrentUserSerializer,
    SetImageUserSerializer,
)


class CurrentUserView(BaseCurrentUser, generics.RetrieveAPIView):
    """
    Получения данных о текущем пользователе.

     Параметры запроса:
    - `No params`: None.

    """
    serializer_class = CurrentUserSerializer


class UpdateCurrentUserView(BaseCurrentUser, generics.UpdateAPIView):
    """
    Обновить данные о текущем пользователе.

     Параметры запроса:
    - `имя пользователя`: str,
    - `адрес электронной почты`: str

    """
    serializer_class = UpdateCurrentUserSerializer


class SetImageUserView(BaseCurrentUser, generics.UpdateAPIView):
    """
    Обновить изображение профиля текущего пользователя.

     Параметры запроса:
    - `в разработке,

    """
    serializer_class = SetImageUserSerializer
