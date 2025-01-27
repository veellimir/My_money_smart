from rest_framework import generics

from .models import MyCategory
from .serializers import CategoryListSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return MyCategory.objects.none()
        return MyCategory.objects.filter(user=user)

