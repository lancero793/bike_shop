from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length= 50)
  reference_code = models.IntegerField()
  description = models.CharField(max_length = 255, default="Dummy Product")
  is_offert = models.BooleanField(default = False)
  size = models.ForeignKey('Sizes', on_delete= models.CASCADE, null = True, blank= True)
  image = models.CharField(max_length = 1025)
  image_one = models.CharField(max_length = 1025)
  image_two = models.CharField(max_length = 1025)
  color = models.ForeignKey('Colour', on_delete= models.CASCADE, blank= True, null = True)
  category = models.ForeignKey('Categories',on_delete = models.CASCADE, blank=True, null = True)
  price = models.IntegerField(default = 0)
  stock = models.IntegerField(default = 0)
  material = models.ForeignKey('Materials', on_delete = models.CASCADE, blank = True, null = True)
  sets_with_warranty = models.ManyToManyField('Warranty', blank = True)
  warranty = models.BooleanField(default= True)
  peso = models.ForeignKey('Weight', on_delete = models.CASCADE, null = True,blank = True)
  duration_warranty = models.ForeignKey('DurationWarranty', on_delete = models.CASCADE, blank = True, default= 1, null= True)
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
class Materials(models.Model):
  material = models.CharField(max_length= 50, default= "Acero", blank = False, null = True)
  def __str__(self):
    return self.material
class Warranty(models.Model):
  with_warranty = models.CharField(max_length = 255, null= True, blank = True)
  def __str__(self):
    return self.with_warranty
class Weight(models.Model):
  peso = models.CharField(max_length = 50, blank= True, default = 0)
  def __str__(self):
    return self.peso
class DurationWarranty(models.Model):
  duration = models.IntegerField(null= False, blank= True, default= 1)
  def __str__(self):
    return f"Garantia {self.duration} Años"
  