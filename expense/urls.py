"""expense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from payments.views import TransactionAPIView, BalanceView, TransactionView, CategoryView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/transactionlist/<int:user_id>', TransactionView.as_view()),
    path("api/balance/<int:user_id>", BalanceView.as_view()),
    path("api/transactionadd/", TransactionView.as_view()),
    path("api/category/", CategoryView.as_view()),
    path("api/category/<int:category_id>", CategoryView.as_view()),
    path('api/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]
