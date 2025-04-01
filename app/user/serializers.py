from rest_framework import serializers

from .models import CustomUser
from app.authentication.utils import *


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'profile_image',
        )

class UpdateCurrentUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
        validators=[validate_username],
    )
    email = serializers.EmailField(
        required=False,
        validators=[validate_email],
    )

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
        )

class SetImageUserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'profile_image',
        )

class PasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, label="Email for password reset")

    def validate_email(self, value):
        try:
            user = CustomUser.objects.get(email=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Пользователь с этим электронным письмом найден не был.")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True, min_length=6)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data