from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer
from EasyProducts.models import Product, Category
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the home of chickens</h1>")

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer