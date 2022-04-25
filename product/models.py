from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

class Product(models.Model):
    Product_Name = models.CharField(max_length=512,blank=False)
    Detail = models.CharField(max_length=2048,blank=False)
    Available = models.BooleanField(default=False)
    Price = models.FloatField(blank=False)
    Product_Image = CloudinaryField('ProductImages', blank=False)
    def __str__(self):
        return self.Product_Name
