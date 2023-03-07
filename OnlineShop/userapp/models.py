from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    ism = models.CharField(max_length=50, blank=True)
    jins = models.CharField(max_length=7, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.ism