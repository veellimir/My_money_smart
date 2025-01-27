from rest_framework import generics

from repository.base_queryset import BasedList
from .models import MyCategory
from .serializers import (
    CreateCategorySerializer,
    CategoryListSerializer
)
from .exceptions import EXCEPTION_CATEGORY_NOT_FOUND


class CreateCategoryView(generics.CreateAPIView):
    serializer_class = CreateCategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteCategoryView(generics.DestroyAPIView):
    serializer_class = CategoryListSerializer
    queryset = MyCategory.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        category = MyCategory.objects.filter(pk=pk, user=self.request.user).first()

        if not category:
            raise EXCEPTION_CATEGORY_NOT_FOUND
        return category


class CategoryListView(BasedList):
    serializer_class = CategoryListSerializer

    def get_model(self):
        return MyCategory
