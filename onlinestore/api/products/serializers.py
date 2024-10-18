from rest_framework.serializers import ModelSerializer
from EasyProducts.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
        

