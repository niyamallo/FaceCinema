from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = None
    last_name = None
    age = models.IntegerField(default=0)