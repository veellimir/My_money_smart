from rest_framework import generics

from .serializers import (
    CurrentUserSerializer,
    UpdateCurrentUserSerializer,
    SetImageUserSerializer,
)


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer

    def get_object(self):
        return self.request.user


class UpdateCurrentUserView(generics.UpdateAPIView):
    serializer_class = UpdateCurrentUserSerializer

    def get_object(self):
        return self.request.user


class SetImageUserView(generics.UpdateAPIView):
    serializer_class = SetImageUserSerializer

    def get_object(self):
        return self.request.user