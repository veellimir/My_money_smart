from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema


from settings.env_config import CONFIG__ALLOWED_HOSTS

from repository.base_queryset import BaseCurrentUser
from .serializers import (
    CurrentUserSerializer,
    UpdateCurrentUserSerializer,
    SetImageUserSerializer,
    PasswordResetEmailSerializer,
    PasswordResetConfirmSerializer
)
from .exсeptions import EXCEPTION_USER_NOT_FOUND
from .models import CustomUser


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


class DeleteCurrentUserView(BaseCurrentUser, generics.DestroyAPIView):
    """
    Удаление текущего пользователя.

    Параметры запроса:
    - `No params`: None.

    Удаляет аккаунт текущего пользователя без возможности восстановления.
    """
    def destroy(self, request, *args, **kwargs) -> Response:
        user: BaseCurrentUser = self.get_object()
        user.delete()
        return Response({"detail": "Пользователь успешно удален"}, status=status.HTTP_204_NO_CONTENT)


class PasswordResetRequestView(BaseCurrentUser, APIView):
    """
    Сброс пароля и отправка письма на email.

    Параметры запроса:
    - `email`: str (обязательный)

    Если пользователь с указанным email существует, отправляется письмо с инструкциями по сбросу пароля.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=PasswordResetEmailSerializer)
    def post(self, request):
        serializer = PasswordResetEmailSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return EXCEPTION_USER_NOT_FOUND
            self.send_reset_email(user)

            return Response(
                {"message": "Вам отправлено письмо с инструкциями по сбросу пароля."},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_reset_email(self, user):
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(str(user.pk).encode())

        reset_url = f"{CONFIG__ALLOWED_HOSTS}/api/v1/user/password-reset-confirm/{uid}/{token}/"

        subject = "Восстановление пароля"
        message = render_to_string(
            'reset-password.html',
            {'reset_url': reset_url, 'user': user}
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], html_message=message)


class PasswordResetConfirmView(APIView):
    """
    Подтверждения сброса пароля.

    Параметры запроса:
    - `uid`: str (идентификатор пользователя, закодированный)
    - `token`: str (токен сброса)
    - `new_password`: str (новый пароль)
    """
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return EXCEPTION_USER_NOT_FOUND

        if not default_token_generator.check_token(user, token):
            return EXCEPTION_USER_NOT_FOUND

        return render(request, 'password-reset-confirm.html', {
            'uidb64': uidb64,
            'token': token
        })

    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return Response({"detail": "Пользователь не найден."}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({"detail": "Неверный токен."}, status=status.HTTP_400_BAD_REQUEST)
        new_password = request.data.get('new_password')

        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Пароль успешно изменен."}, status=status.HTTP_200_OK)

        return Response({"detail": "Новый пароль не был передан."}, status=status.HTTP_400_BAD_REQUEST)


def final_password(request):
    return render(request, "final_password.html")


def politics_page(request):
    return render(request, "politics.html")