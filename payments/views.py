from django.shortcuts import render
from rest_framework import generics
from payments.models import Transaction, Category
from payments.serializers import TransactionSerializer


class TransactionAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
