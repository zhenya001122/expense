from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория расходов',
                            blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    summ = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время транзакции')
    organization = models.CharField(max_length=30, verbose_name='Организация')
    description = models.CharField(max_length=100, verbose_name='Описание')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="transactions", on_delete=models.CASCADE
    )
    category = models.ForeignKey(Category, related_name="transactions", on_delete=models.CASCADE)

    class Meta:
        ordering = ['summ', '-time_create']

    def __str__(self):
        return f"{self.summ} {self.user}"


class Balance(models.Model):
    summ = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ваш баланс')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="balances", on_delete=models.CASCADE
    )
    transaction = models.ForeignKey(Transaction, related_name="balances", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.summ} {self.user}"
