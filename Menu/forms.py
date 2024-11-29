from django import forms
from .models import *

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('customer','total_amount','description','duration','is_paid')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','email','phone')



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        
        
class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"
