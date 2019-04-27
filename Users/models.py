from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name =  models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    username = models.CharField(unique=True,max_length=20, primary_key=True)
    email = models.EmailField(unique=True,max_length=50)
    last_name = models.CharField(max_length=50)