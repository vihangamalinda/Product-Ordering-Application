from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from accounts.models import *


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    customer_count = Customer.objects.all().count()
    order_count = Order.objects.all().count()
    delivered = Order.objects.all().filter(status="Delivered").count()
    pending = Order.objects.all().filter(status="Pending").count()

    context = {"customers": customers, "orders": orders, "customer_count": customer_count, "order_count": order_count,
               "delivered": delivered, "pending": pending}
    return render(request, "accounts/dashboard.html", context)


def product(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {"products": products})


def customer(request):
    return render(request, "accounts/customer.html")
