
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): # Subclassing Django's User model for customization
    dob = models.DateField()

class Location(models.Model):
    name = models.CharField(max_length=45)
    state = models.CharField(max_length=45)

class Hotspot(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    distance = models.IntegerField()



class Hotel(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    capacity = models.IntegerField() #total cap
    occupancy = models.IntegerField()

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Itenary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
