from rest_framework import serializers

from .models import MyCategory, MyFinance


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


class CreateOperationSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        input_formats=['%d.%m.%Y'],
        format='%d.%m.%Y',
    )

    class Meta:
        model = MyFinance
        fields = [
            'category',
            'amount',
            'date',
            'transaction_type'
        ]


class IncomeListSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        input_formats=['%d.%m.%Y'],
        format='%d.%m.%Y',
    )

    class Meta:
        model = MyFinance
        fields = [
            'id',
            'category',
            'amount',
            'date',
            'transaction_type'
        ]
