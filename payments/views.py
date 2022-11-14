from payments.models import Transaction, Category, Balance
from payments.serializers import TransactionSerializer, BalanceSerializer
from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status, generics


class TransactionAPIView(generics.ListAPIView):
    """
    Возвращает список всех транзакций
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionView(APIView):
    """
    Возвращает список транзакций пользователя
    """
    def get(self, request: HttpRequest, user_id: int) -> Response:
        transaction = Transaction.objects.filter(user=user_id)
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
    """
    Добавляет транзакцию в БД и обновляет баланс после проведения транзакции
    """
    def post(self, request: HttpRequest) -> Response:
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            transaction = Transaction.objects.last()
            balance = Balance.objects.get(user=transaction.user.id)
            if transaction.category.name == "Доход":
                balance.summ += transaction.summ
                balance.save()
            else:
                balance.summ -= transaction.summ
                balance.save()
            return Response({"serializer.data": 200, "status": status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BalanceView(APIView):
    """
    Возвращает баланс пользователя
    """

    def get(self, request: HttpRequest, user_id: int, format=None) -> Response:
        balance = Balance.objects.get(user=user_id)
        serializer = BalanceSerializer(balance)
        return Response(serializer.data)


class CategoryView(APIView):
    pass
