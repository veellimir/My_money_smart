from django.core.exceptions import ValidationError

from rest_framework.response import Response
from rest_framework import status


EXCEPTION_USER_NOT_FOUND = Response(
    {"detail": "Введите корректный email"},
    status=status.HTTP_400_BAD_REQUEST
)