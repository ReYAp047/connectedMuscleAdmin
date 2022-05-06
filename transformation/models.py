
from django.db import models

class transformation(models.Model):
    Member_Email = models.EmailField(blank=False)
    Week_Date = models.DateField(blank=False)
    Week_Goal = models.CharField(max_length=512,default=False)
    Body_Height = models.FloatField(default=False)
    Body_Weight = models.FloatField(default=False)
    Image_Link = models.CharField(max_length=512,default=False)
    def __str__(self):
        return self.Member_Email
