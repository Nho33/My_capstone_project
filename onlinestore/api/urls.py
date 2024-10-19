#from rest_framework.routers import DefaultRouter
from django.urls import path
from api.products.views import ProductList, ProductDetail, CategoryList, CategoryDetail
from api.users.views import CustomerList, CustomerDetail, OrderList, OrderDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
