from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length= 50)
  reference_code = models.IntegerField()
  description = models.CharField(max_length = 255, default="Dummy Product")
  is_offert = models.BooleanField(default = False)
  size = models.ForeignKey('Sizes', on_delete= models.CASCADE, null = True, blank= True)
  image = models.CharField(max_length = 1025)
  color = models.ForeignKey('Colour', on_delete= models.CASCADE, blank= True, null = True)
  category = models.ForeignKey('Categories',on_delete = models.CASCADE, blank=True, null = True)
  price = models.IntegerField(default = 0)
  stock = models.IntegerField(default = 0)
  def __str__(self):
    return str(self.name)
class Sizes(models.Model):
    SIZES_OPTIONS = (
    ("XS", "EXTRA SMALL"),
    ("S", "SMALL"),
    ("M", "MEDIUM"),
    ("L", "LARGE"),
    )
    sizes = models.CharField(max_length= 2, choices= SIZES_OPTIONS)
    def __str__(self):
      return self.sizes
class Categories(models.Model):
  CATEGORIE_PRODUCT = (
    ("IND", "INDUMENTARIA"),
    ("MTB", "MTB"),
    ("BMX", "BMX"),
    )
  category = models.CharField(max_length=3, choices= CATEGORIE_PRODUCT)
  def __str__(self):
    return self.category
class Colour(models.Model):
  color = models.CharField(max_length= 30, blank= True)
  def __str__(self):
    return self.color

