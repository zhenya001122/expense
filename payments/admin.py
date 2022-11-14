from django.contrib import admin

from payments.models import Category, Transaction, Balance


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('summ', 'time_create', 'organization', 'description', 'user', 'category')
    list_filter = ('summ', 'time_create')
    search_fields = ('summ', 'time_create', 'user', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', "user")


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('summ', "user")
