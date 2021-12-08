from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home(request):
    all_products = Product.objects.all()
    return render(request, "index.html", {"products" : all_products})

def products(request):
    products_all = Product.objects.all()
   # product_last_created = Product.objects.all()[2:]
  
    return render(request, "products.html",
    {"products" : products_all,
     "last" : None,
    })

def contact(request):
    return render(request, "contact.html")

def about(request):
  return render(request, "about.html")
  
# Vista utilizada para mostrar la vista de productos
def details(request, product_id):
  product = Product.objects.get(id= product_id)
  return render(request, "product.html", 
 {"product" : product})
