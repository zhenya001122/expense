from rest_framework import serializers
from payments.models import Transaction, Balance, Category


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('summ',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "user")

        def create(self, validated_data):
            return Category.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get("name", instance.name)
            instance.user = validated_data.get("user", instance.user)
            instance.save()
            return instance
