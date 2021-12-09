from django.contrib import admin

# Register your models here.
from .models import (
  Product,
  Colour,
  Sizes,
  Categories,
  Warranty,
  Weight,
  Materials,
  DurationWarranty,
  )
admin.site.register(Product)
admin.site.register(Colour)
admin.site.register(Sizes)
admin.site.register(Categories)
admin.site.register(Warranty)
admin.site.register(Weight)
admin.site.register(Materials)
admin.site.register(DurationWarranty)
