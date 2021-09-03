from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from accounts.models import *
from .forms import OrderForm


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


def customer(request, pk_id):
    customer = Customer.objects.get(id=pk_id)
    orders = customer.order_set.all()
    order_count = customer.order_set.all().count()

    context = {"customer": customer, "orders": orders, "order_count": order_count}
    return render(request, "accounts/customer.html", context)


def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        # print(" ")
        # print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk_id):
    order = Order.objects.get(id=pk_id)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk_id):
    item = Order.objects.get(id=pk_id)
    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {"item": item}
    return render(request, "accounts/delete.html", context)
