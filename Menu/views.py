from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,TemplateView
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request) 
    return render(request, 'registration/log_out.html') 

def login(request):
    return redirect("accounts/login/")


class Base(TemplateView):
    template_name = "base.html"


# Order

class LoanListView(ListView):
    model = Loan
    template_name = 'o_list.html'




class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'o_cr.html'
    success_url = reverse_lazy('o_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'o_up.html'
    success_url = reverse_lazy('o_list')
    
    def get_queryset(self):
        return Loan.objects.filter(user = self.request.user)

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'o_delete.html'
    success_url = reverse_lazy('order-list')
    
    def get_queryset(self):
        return Loan.objects.filter(user = self.request.user)

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'o_detail.html'
    context_object_name = "object"


# Customer
class CustomerListView(ListView):
    model = Customer
    template_name = 'c_list.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'c_cr.html'
    success_url = reverse_lazy('c_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'c_up.html'
    success_url = reverse_lazy('c_list')
    def get_queryset(self):
        return Customer.objects.filter(user = self.request.user)

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'c_delete.html'
    success_url = reverse_lazy('c_list')
    
    def get_queryset(self):
        return Customer.objects.filter(user = self.request.user)

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'c_detail.html'
    context_object_name = "object"

# Product
class PaymentListView(ListView):
    model = Payment
    template_name = 'p_list.html'


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'p_cr.html'
    success_url = reverse_lazy('p_list')


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'p_up.html'
    success_url = reverse_lazy('p_list')
    


class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'p_delete.html'
    success_url = reverse_lazy('p_list')


class PaymentDetailView(DetailView):
    model = Payment
    
    
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context["vakansi"] = Order.objects.filter(product = self.kwargs['pk'])
    #     return context
    
    
    template_name = 'p_detail.html'
    context_object_name = "object"
    
    
# Wallet
class WalletListView(ListView):
    model = Wallet
    template_name = 'w_list.html'


class WalletCreateView(CreateView):
    model = Wallet
    form_class = WalletForm
    template_name = 'w_cr.html'
    success_url = reverse_lazy('w_list')
    


class WalletUpdateView(UpdateView):
    model = Wallet
    form_class = WalletForm
    template_name = 'w_up.html'
    success_url = reverse_lazy('w_list')
    


class WalletDeleteView(DeleteView):
    model = Wallet
    template_name = 'w_delete.html'
    success_url = reverse_lazy('w_list')


class WalletDetailView(DetailView):
    model = Wallet
    
    
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context["vakansi"] = Order.objects.filter(product = self.kwargs['pk'])
    #     return context
    
    
    template_name = 'w_detail.html'
    context_object_name = "object"