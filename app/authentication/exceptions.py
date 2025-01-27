from django.core.exceptions import ValidationError

from rest_framework.response import Response
from rest_framework import status


EXCEPTION_USERNAME_ALREADY_EXISTS = Response(
    {"Error": "Пользователь с таким именем уже существует !"},
    status=status.HTTP_409_CONFLICT,
)

EXCEPTION_EMAIL_ALREADY_EXISTS = Response(
    {"Error": "Пользователь с таким email уже существует !"},
    status=status.HTTP_409_CONFLICT,
)

EXCEPTION_USER_PASSWORD = Response(
    {"error": "Текущий пароль неверен или новый пароль не совпадает."},
    status=status.HTTP_400_BAD_REQUEST
)

EXCEPTION_PASSWORD_CONFLICT = ValidationError(
    {"Error": "Пароли не совпадают !"},
)

EXCEPTION_ERROR_PASSWORD = ValidationError(
    "Имя пользователя должно состоять только из букв "
    "Английского алфавита Aa-Zz и содержать от 4 до 20 символов."
)

EXCEPTION_QUANTITY_PASSWORD = ValidationError(
    "Пароль должен содержать не менее 6 символов"
)

EXCEPTION_LETTERS_PASSWORD = ValidationError(
    "Пароль должен содержать хотя бы одну букву."
)

EXCEPTION_DIGIT_PASSWORD = ValidationError(
    "Пароль должен содержать хотя бы одну цифру."
)

EXCEPTION_INCORRECT_EMAIL = ValidationError(
    "Введите корректный адрес электронной почты"
)