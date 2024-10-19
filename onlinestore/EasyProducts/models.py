from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.
#Category model has to appear before the product model otherwise it will give a NameError

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
#Product mode
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #when a category is deleted, all related products will be deleted as well.
    stock = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    

