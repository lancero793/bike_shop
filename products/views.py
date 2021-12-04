from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home(request):
    all_products = Product.objects.all()
    return render(request, "index.html", {"products" : all_products})

def products(request):
    return render(request, "products.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
  return render(request, "about.html")
def details(request, product_id):
  return HttpResponse("Mensaje desde %s" %product_id)

def product(request):
    return render(request, "product.html")