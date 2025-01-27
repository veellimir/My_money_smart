from rest_framework import serializers

from .models import MyCategory


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCategory
        fields = [
            'id',
            'title'
        ]
