from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def product(request):
    return render(request, "product.html")