"""
URL configuration for Shop_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from shop_user_app.views import main_page, buy_product, product_info

app_name = 'user_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('<int:product_id>', buy_product, name='buy'),
    path('product_info/<int:product_id>/', product_info),
]
