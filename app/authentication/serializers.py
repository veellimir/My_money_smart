from typing import Dict

from rest_framework import serializers
from django.contrib.auth.models import User

from .exceptions import EXCEPTION_PASSWORD_CONFLICT
from .utils import *


class RegisterUserSerializer(serializers.ModelSerializer):
    username: str = serializers.CharField(
        required=True,
        validators=[validate_username],
    )
    password: str = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    confirm_password: str = serializers.CharField(
        write_only=True,
        required=True,
    )
    email: str = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_email],
    )

    class Meta:
        model = User
        fields: tuple = (
            'username',
            'password',
            'confirm_password',
            'email',
        )

    def validate(self, attrs) -> str:
        if attrs['password'] != attrs['confirm_password']:
            raise EXCEPTION_PASSWORD_CONFLICT
        return attrs

    def create(self, validated_data: Dict[str, str]) -> User:
        validated_data.pop('confirm_password')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class NewUserPasswordSerializer(serializers.ModelSerializer):
    old_password: str = serializers.CharField(required=True)
    new_password: str = serializers.CharField(required=True)
    confirm_password: str = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password',
            'confirm_password',
        )