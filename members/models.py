from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Members(AbstractUser):
    street = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.pk
