from django.shortcuts import render

from .models import Product

def home(request):
    context = { "title": "Home" }
    return render(request, "shop/home.html", context=context)

def all(request):
    all_products = Product.objects.order_by("-stock")
    context = {
        "title": "Shop All",
        "all_products": all_products
    }
    return render(request, "shop/all.html", context=context)

def detail(request, product_id):
    context = { "title": f"{product_id}" }
    return render(request, "shop/detail.html", context=context)
