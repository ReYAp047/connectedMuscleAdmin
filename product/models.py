from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

class ProductCategory(models.Model):
    Titre = models.CharField(max_length=50, blank=False, primary_key=True)
    def __str__(self):
        return self.Titre

class Product(models.Model):
    Product_Name = models.CharField(max_length=512,blank=False)
    Detail = models.CharField(max_length=2048,blank=False)
    Category = models.ForeignKey(ProductCategory, blank=False, default=None, on_delete=models.CASCADE)
    Available = models.BooleanField(default=False)
    Price = models.FloatField(blank=False)
    Product_Image = CloudinaryField('ProductImages', blank=False)
    Recommended = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return self.Product_Name
