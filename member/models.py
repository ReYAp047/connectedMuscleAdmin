from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

class Member(models.Model):
    Member_Name = models.CharField(max_length=512,blank=False)
    Email = models.EmailField(blank=False)
    Password = models.CharField(max_length=512,blank=False)
    Birth_Day = models.DateField(blank=False)
    Bodybuilding = models.BooleanField(default=False)
    Cardio = models.BooleanField(default=False)
    Courses = models.BooleanField(default=False)
    Subscription_expire_Date = models.DateField(blank=False)
    def __str__(self):
        return self.Member_Name
