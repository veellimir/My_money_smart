from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterUserSerializer
from .exceptions import (
    EXCEPTION_USERNAME_ALREADY_EXISTS,
    EXCEPTION_EMAIL_ALREADY_EXISTS,
)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs) -> Response:
        username: str = request.data.get('username')
        email: str = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return EXCEPTION_USERNAME_ALREADY_EXISTS
        if User.objects.filter(email=email).exists():
            return EXCEPTION_EMAIL_ALREADY_EXISTS

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"Message": "Пользователь успешно зарегистрирован !"},
            status=status.HTTP_201_CREATED,
        )
