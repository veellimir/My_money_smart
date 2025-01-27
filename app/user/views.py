from rest_framework import generics

from repository.base_queryset import BaseCurrentUser
from .serializers import (
    CurrentUserSerializer,
    UpdateCurrentUserSerializer,
    SetImageUserSerializer,
)


class CurrentUserView(BaseCurrentUser, generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer


class UpdateCurrentUserView(BaseCurrentUser, generics.UpdateAPIView):
    serializer_class = UpdateCurrentUserSerializer


class SetImageUserView(BaseCurrentUser, generics.UpdateAPIView):
    serializer_class = SetImageUserSerializer
