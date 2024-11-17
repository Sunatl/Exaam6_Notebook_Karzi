from django.urls import path
from .views import *
urlpatterns = [
    # Base page
    path('Home', Base.as_view(), name='base'),
    path("",login,name="login"),


    # Loan
    path('loan/', LoanListView.as_view(), name='o_list'),
    path('loan/create/', LoanCreateView.as_view(), name='o_cr'),
    path('loan/update/<int:pk>/', LoanUpdateView.as_view(), name='o_up'),
    path('loan/delete/<int:pk>/', LoanDeleteView.as_view(), name='o_delete'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='o_detail'),

    # Customer
    path('customers/', CustomerListView.as_view(), name='c_list'),
    path('customer/create/', CustomerCreateView.as_view(), name='c_cr'),
    path('customer/update/<int:pk>/', CustomerUpdateView.as_view(), name='c_up'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='c_delete'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='c_detail'),

    # Payment
    path('payments/', PaymentListView.as_view(), name='p_list'),
    path('payment/create/', PaymentCreateView.as_view(), name='p_cr'),
    path('payment/update/<int:pk>/', PaymentUpdateView.as_view(), name='p_up'),
    path('payment/delete/<int:pk>/', PaymentDeleteView.as_view(), name='p_delete'),
    path('payment/<int:pk>/', PaymentDetailView.as_view(), name='p_detail'),

    # Wallet
    path('wallets/', WalletListView.as_view(), name='w_list'),
    path('wallet/create/', WalletCreateView.as_view(), name='w_cr'),
    path('wallet/update/<int:pk>/', WalletUpdateView.as_view(), name='w_up'),
    path('wallet/delete/<int:pk>/', WalletDeleteView.as_view(), name='w_delete'),
    path('wallet/<int:pk>/', WalletDetailView.as_view(), name='w_detail'),

    # Logout
    path('logout/', user_logout, name='logout'),
]
