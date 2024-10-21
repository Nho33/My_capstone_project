from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer
from EasyProducts.models import Product, Category
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the home of chickens</h1>")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
