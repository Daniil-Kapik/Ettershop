from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Ettershop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Ettershop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
