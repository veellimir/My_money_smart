from django.db import models

from app.user.models import CustomUser


class MyCategory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=100, )


class MyFinance(models.Model):
    OPERATIONS = (
        ("income", "Income", ),
        ("expense", "Expense", ),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='finances')
    category = models.ForeignKey(
        MyCategory,
        on_delete=models.CASCADE,
        related_name='finances',
        blank=True,
        null=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    transaction_type = models.CharField(
        max_length=20,
        choices=OPERATIONS,
        default='expense'
    )
