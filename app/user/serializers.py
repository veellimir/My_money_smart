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