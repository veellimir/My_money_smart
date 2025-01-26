from rest_framework import generics
from rest_framework.response import Response

from .serializers import CurrentUserSerializer


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer

    def get_object(self) -> Response:
        return self.request.user
