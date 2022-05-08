from django.db import models
from cloudinary.models import CloudinaryField

class Chest(models.Model):
    Exercise_Name = models.CharField(max_length=512,blank=False)
    Repetition = models.CharField(max_length=512,blank=False)
    Product_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Exercise_Name

class Back(models.Model):
    Exercise_Name = models.CharField(max_length=512,blank=False)
    Repetition = models.CharField(max_length=512,blank=False)
    Product_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Exercise_Name        

class Shoulders(models.Model):
    Exercise_Name = models.CharField(max_length=512,blank=False)
    Repetition = models.CharField(max_length=512,blank=False)
    Product_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Exercise_Name

class Legs(models.Model):
    Exercise_Name = models.CharField(max_length=512,blank=False)
    Repetition = models.CharField(max_length=512,blank=False)
    Product_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Exercise_Name

class Biceps(models.Model):
    Exercise_Name = models.CharField(max_length=512,blank=False)
    Repetition = models.CharField(max_length=512,blank=False)
    Product_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Exercise_Name        

class Triceps(models.Model):
    Exercise_Name = models.CharField(max_length=512,blank=False)
    Repetition = models.CharField(max_length=512,blank=False)
    Product_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Exercise_Name

class Cardio(models.Model):
    Exercise_Name = models.CharField(max_length=512,blank=False)
    Repetition = models.CharField(max_length=512,blank=False)
    Product_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Exercise_Name        

class Programme(models.Model):
    Programme_Name = models.CharField(max_length=512,blank=False)
    Programme_Image = CloudinaryField('ExercisesImages', blank=False)
    def __str__(self):
        return self.Programme_Name