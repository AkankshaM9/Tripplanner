
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser): # Subclassing Django's User model for customization
    dob = models.DateField()


class Itenary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
