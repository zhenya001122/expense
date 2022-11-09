from django.shortcuts import render
from rest_framework import generics
from payments.models import Transaction, Category, Balance
from payments.serializers import TransactionSerializer, BalanceSerializer
from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework import status


class TransactionView(APIView):
    def post(self, request: HttpRequest) -> Response:
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"serializer.data": 200, "status": status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
