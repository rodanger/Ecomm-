from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('product-detail/<int:id>',views.product_detail,name='product-detail'),
    path('Login',views.Login,name='Login'),
    path('Signup',views.Signup,name='Signup'),
    path('cart',views.cart,name='cart'),
    path('save_order',views.save_order,name='save_order'),
    path('myorders',views.myorders,name='myorders'),
    path('remove/<int:id>',views.remove,name='remove'),
]