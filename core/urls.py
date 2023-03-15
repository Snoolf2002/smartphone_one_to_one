"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from api.views import add_product, get_product, get_with_model, get_with_price_gt, get_with_price_lt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', get_product),
    path('api/model/<str:model>', get_with_model),
    path('api/add/product', add_product),
    path('api/price/gt/<str:gt>', get_with_price_gt),
    path('api/price/lt/<str:lt>', get_with_price_lt),

]
