from rest_framework import generics

from repository.base_queryset import BasedList
from .models import MyCategory
from .serializers import (
    CreateCategorySerializer,
    CategoryListSerializer
)


class CreateCategoryView(generics.CreateAPIView):
    serializer_class = CreateCategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryListView(BasedList):
    serializer_class = CategoryListSerializer

    def get_model(self):
        return MyCategory
