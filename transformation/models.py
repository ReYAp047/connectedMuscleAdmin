from tkinter import Image
from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

class transformation(models.Model):
    Member_Email = models.CharField(max_length=512,blank=False)
    Week_Date = models.DateField(blank=False)
    Week_Goal = models.CharField(default=False)
    Body_Height = models.FloatField(default=False)
    Body_Weight = models.FloatField(default=False)
    Image_Link = models.URLField(blank=False)
    def __str__(self):
        return self.Member_Email
