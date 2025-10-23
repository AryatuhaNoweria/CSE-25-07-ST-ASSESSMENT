from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    REQUIRED_FIELDS = ['full_name', 'phone_number']
    USERNAME_FIELD = 'email'  # now you login with email

    def __str__(self):
        return self.email
