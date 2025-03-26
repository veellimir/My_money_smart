from rest_framework import serializers

from .models import MyFinance


class CreateOperationSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        input_formats=['%d.%m.%Y'],
        format='%d.%m.%Y',
    )

    class Meta:
        model = MyFinance
        fields = [
            'amount',
            'date',
            'transaction_type'
        ]


class OperationListSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        input_formats=['%d.%m.%Y'],
        format='%d.%m.%Y',
    )

    class Meta:
        model = MyFinance
        fields = [
            'id',
            'amount',
            'date',
            'transaction_type'
        ]
