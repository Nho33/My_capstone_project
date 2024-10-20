"""
URL configuration for onlinestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.products.views import home_view
from api.users.views import RegisterView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('api.urls')),
    path('', home_view, name='home'),
    path('auth/', include('dj_rest_auth.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),  # Login, Logout, Password reset
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # For users to Register
    path('accounts/', include('allauth.urls')), 
    path('register/', RegisterView.as_view(), name='register'),  # Registration page
    path('logout/', LogoutView.as_view(), name='logout'),

]
