from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("contactenos/", views.contact, name="contactenos"),
    path("nosotros/", views.about, name="nosotros"),
    path("products/<int:product_id>/", views.details, name="info-product"),
]