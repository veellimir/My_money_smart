from rest_framework import serializers

from .models import MyCategory


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCategory
        fields = ['title']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCategory
        fields = [
            'id',
            'title'
        ]
