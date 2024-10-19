from rest_framework.serializers import ModelSerializer
from EasyProducts.models import Product, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
        

