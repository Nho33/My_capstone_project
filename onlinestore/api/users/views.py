from rest_framework import viewsets
from EasyUsers.models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated




class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]  
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(AuthLoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'
