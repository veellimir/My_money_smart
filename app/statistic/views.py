from datetime import datetime

from django.db.models import Sum

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app.finance.models import MyFinance


class StatisticView(APIView):
    """
    Получения статистики по категориям за определенный период.

     Параметры запроса:
    - `date` (строка) – в формате `YYYY-MM-DD_YYYY-MM-DD`.

    Пример запроса:
    - `GET server/api/v1/statistics/list/2025-01-01_2025-01-31/`
    """
    def get(self, request, date) -> Response:
        try:
            start_date, end_date = date.split('_')
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD_YYYY-MM-DD"},
                            status=status.HTTP_400_BAD_REQUEST)
        stats = (
            MyFinance.objects
            .values('category__title')
            .annotate(total_amount=Sum('amount'))
            .order_by('-total_amount')
        )

        data: list = [
            {"category_name": stat["category__title"], "total_amount": stat["total_amount"]}
            for stat in stats
        ]
        return Response(data, status=status.HTTP_200_OK)