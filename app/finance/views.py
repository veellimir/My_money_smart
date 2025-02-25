from rest_framework import generics

from repository.base_queryset import BasedList
from .models import MyCategory, MyFinance
from .serializers import (
    CreateCategorySerializer,
    CategoryListSerializer,
    CreateOperationSerializer,
    OperationListSerializer,
)
from .exceptions import EXCEPTION_CATEGORY_NOT_FOUND
from utils.exceptions import EXCEPTION_INVALID_FILTER


class CreateCategoryView(generics.CreateAPIView):
    """
    Создать категорию по списанию средств

    Параметры запроса:
    - `наименование категории`: str,

    """
    serializer_class = CreateCategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteCategoryView(generics.DestroyAPIView):
    """
    Удалить категорию списание средств по id

    Параметры запроса:
    - `id категории`: int,

    """
    serializer_class = CategoryListSerializer
    queryset = MyCategory.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        category = MyCategory.objects.filter(pk=pk, user=self.request.user).first()

        if not category:
            raise EXCEPTION_CATEGORY_NOT_FOUND
        return category


class CategoryListView(BasedList):
    """
    Получить список категорий списания средств

    Параметры запроса:
    - `No params`: None,

    """
    serializer_class = CategoryListSerializer

    def get_model(self):
        return MyCategory


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
