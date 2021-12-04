from django.db import models

# Create your models here.
class Product(models.Model):
  SIZES_OPTIONS = (
    ("XS", "EXTRA SMALL"),
    ("S", "SMALL"),
    ("M", "MEDIUM"),
    ("L", "LARGE"),
    )
  name = models.CharField(max_length= 50)
  reference_code = models.IntegerField()
  description = models.CharField(max_length = 255, default="Dummy Product")
  is_offert = models.BooleanField(default = False)
  size = models.CharField(choices=SIZES_OPTIONS, max_length  = 2)
  image = models.CharField(max_length = 1025)
  price = models.IntegerField(default = 0)
  stock = models.IntegerField(default = 0)
  def __str__(self):
    return str(self.name)
    

