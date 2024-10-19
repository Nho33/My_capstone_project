from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from EasyProducts.models import Product

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password,):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=20)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Profile(models.Model):
    pic = models.URLField() #we will not keep pictures in our database thus we will use a url to locate it from a storage
    address = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #One user can only have one profile and a profile can only belong to one user
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    pic = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.surname}'
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True) # Only adds the date that the order is initially made. The date does not update every time the order is updated.
    shipped_date = models.DateTimeField(null=True, blank=True)
    is_paid = models.BooleanField(default=False) 

    def __str__(self):
        return f'Order {self.id} by {self.customer}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'