from django.contrib import admin
from .models import Customer, Wallet, Loan, Payment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')  
    list_filter = ('created_at',)  

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('customer', 'balance')
    search_fields = ('customer__name',)  
    list_filter = ('balance',)  

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'is_paid', 'created_at')
    search_fields = ('customer__name', 'description')
    list_filter = ('is_paid', 'created_at')



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'amount', 'payment_date', 'description')
    search_fields = ('loan__customer__name', 'description')
    list_filter = ('payment_date',)

