from rest_framework import viewsets
from .serializers import ProductSerializer
from EasyProducts.models import Product
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the home of chickens</h1>")

class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()