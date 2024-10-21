from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.products.views import ProductViewSet, CategoryViewSet
from api.users.views import CustomerViewSet, OrderViewSet, RegisterView, LoginView, LogoutView

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('categories',CategoryViewSet, basename='category')
router.register('customers', CustomerViewSet, basename='customer')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
   # path('products/', ProductList.as_view(), name='product-list'),
   # path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
  #  path('categories/', CategoryList.as_view(), name='category-list'),
   # path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
   # path('customers/', CustomerList.as_view(), name='customer-list'),
   # path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
   # path('orders/', OrderList.as_view(), name='order-list'),
   # path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
   path('register/', RegisterView.as_view(), name='register'),  # Registration page
   path('login/', LoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
]
