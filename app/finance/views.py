from rest_framework import generics

from repository.base_queryset import BasedList
from .models import MyFinance
from .serializers import (
    CreateOperationSerializer,
    OperationListSerializer,
)
from .exceptions import EXCEPTION_CATEGORY_NOT_FOUND
from utils.exceptions import EXCEPTION_INVALID_FILTER


class CreateOperationView(generics.CreateAPIView):
    """
    Создание операции по затратам или зачислениям

    Параметры запроса при списание средств:

    - `id категории`: int,
    - `сумма списания`: int,
    - `дата операции`: str(30.01.2025),
    - `тип операции`: str(expense)

    Параметры запроса при зачислении средств:

    - `id категории`: null,
    - `сумма зачисления`: int,
    - `дата операции`: str(30.01.2025),
    - `тип операции`: str(income),

    """
    serializer_class = CreateOperationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FinanceListView(BasedList):
    """
       Получить список операций с фильтрацией

       Параметры запроса:
       - `фильтр`: all: все | expense: списания | income: зачисления,

       """
    serializer_class = OperationListSerializer

    def get_model(self):
        return MyFinance

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_param = self.kwargs.get('filter_params')

        if filter_param.lower() in 'all':
            return queryset
        if filter_param:
            if filter_param.lower() in ['income', 'expense']:
                queryset = queryset.filter(transaction_type=filter_param.lower())
            else:
                raise EXCEPTION_INVALID_FILTER
        return queryset
