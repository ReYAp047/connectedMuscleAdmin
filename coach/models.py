from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField


class Coach(models.Model):
    Coach_Name = models.CharField(max_length=512,blank=False)
    Coaching_specialtie = models.CharField(max_length=2048,blank=False)
    Private_coaching = models.BooleanField(default=False)
    Coaching_Price = models.FloatField(blank=False)
    Coach_Photo = CloudinaryField('ProductImages', blank=False)
    def __str__(self):
        return self.Coach_Name
