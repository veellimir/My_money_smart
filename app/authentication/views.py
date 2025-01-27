from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .serializers import RegisterUserSerializer, NewUserPasswordSerializer
from .utils import validate_password
from .exceptions import (
    EXCEPTION_USERNAME_ALREADY_EXISTS,
    EXCEPTION_EMAIL_ALREADY_EXISTS,
    EXCEPTION_USER_PASSWORD,
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


class NewUserPasswordView(generics.UpdateAPIView):
    serializer_class = NewUserPasswordSerializer

    def update(self, request, *args, **kwargs) -> Response | None:
        if getattr(self, 'swagger_fake_view', False):
            return None
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: User = request.user
        old_password: str = serializer.validated_data['old_password']
        new_password: str = serializer.validated_data['new_password']

        if not user.check_password(old_password):
            return EXCEPTION_USER_PASSWORD

        try:
            validate_password(new_password)
        except ValidationError as e:
            return Response(
                {"Error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.set_password(new_password)
        user.save()

        return Response(
            {"Message": "Пароль был успешно изменен."},
            status=status.HTTP_200_OK
        )