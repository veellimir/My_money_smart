from rest_framework import generics


class BasedList(generics.ListAPIView):
    def get_queryset(self):
        """
        Получаем объекты текущего пользователя.
        """
        user = self.request.user
        if not user.is_authenticated:
            return self.get_model().objects.none()
        return self.get_model().objects.filter(user=user)

    def get_model(self):
        """
        Этот метод должен быть переопределён в дочернем классе,
        чтобы вернуть модель, с которой нужно работать.
        """
        raise NotImplementedError("get_model() must be implemented in the subclass.")


class BaseCurrentUser(generics.GenericAPIView):
    """
    Базовый класс для представлений, работающих с текущим пользователем.
    """
    def get_object(self):
        """
        Метод для получения текущего пользователя.
        """
        return self.request.user