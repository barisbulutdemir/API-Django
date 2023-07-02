from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Ek alanlarınızı buraya ekleyin
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

