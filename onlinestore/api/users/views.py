from rest_framework import generics
from EasyUsers.models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        super().form_valid(form)
        return redirect('login')

def register(request):
    return render(request, 'registration.html')

class LoginView(AuthLoginView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'
