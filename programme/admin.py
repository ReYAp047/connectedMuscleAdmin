from django.contrib import admin
from programme.models import Chest, Back, Shoulders, Legs, Biceps, Triceps, Cardio, Programme

admin.site.register([Chest, Back, Shoulders, Legs, Biceps, Triceps, Cardio, Programme])
