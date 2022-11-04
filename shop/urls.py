"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('product-detail/<int:id>',views.product_detail,name='product-detail'),
    path('Login',views.Login,name='Login'),
    path('Signup',views.Signup,name='Signup'),
    path('cart',views.cart,name='cart'),
    path('myorders',views.myorders,name='myorders'),
    path('save_order',views.save_order,name='save_order'),
    path('remove/<int:id>',views.remove,name='remove'),

]

