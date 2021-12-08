from django.contrib import admin

# Register your models here.
from .models import (
  Product,
  Colour,
  Sizes,
  Categories,
  )
admin.site.register(Product)
admin.site.register(Colour)
admin.site.register(Sizes)
admin.site.register(Categories)