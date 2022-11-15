from payments.models import Transaction, Category, Balance
from payments.serializers import TransactionSerializer, BalanceSerializer, CategorySerializer
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
        if serializer.is_valid(raise_exception=True):
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
    def post(self, request):
        """Добавляет категорию пользователю"""
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, category_id):
        """Изменяет существующую категорию пользователя"""
        if not category_id:
            return Response({"error": "Метод PUT не разрешен"})

        try:
            instance = Category.objects.get(id=category_id)
        except:
            return Response({"error": "Объект не существует"})

        serializer = CategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, category_id):
        """Удаляет категорию пользователя"""
        if not category_id:
            return Response({"error": "Метод DELETE не разрешен"})

        category = Category.objects.get(id=category_id)
        category.delete()

        return Response({"post": "Удалена запись " + str(category_id)})
