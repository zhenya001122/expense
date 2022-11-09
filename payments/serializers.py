from rest_framework import serializers
from payments.models import Transaction, Balance


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('summ',)
