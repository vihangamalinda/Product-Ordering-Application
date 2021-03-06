from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.product, name="products"),
    path('customer/<str:pk_id>/', views.customer,name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk_id>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk_id>/', views.deleteOrder, name="delete_order"),

]
