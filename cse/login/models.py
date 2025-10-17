from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    Full_Name = models.CharField(max_length=255)
    Email =models.EmailField()
    Phone_Number =models.CharField()
    Password1 = models. CharField()
    Password2 = models.CharField()

def __str__(self):
    return self.Full_Name
